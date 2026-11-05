#!/usr/bin/env python3
"""Add Android TV launcher support to a Capacitor Android manifest."""
from pathlib import Path
import re
import sys

manifest = Path("android/app/src/main/AndroidManifest.xml")
if not manifest.is_file():
    sys.exit(
        "ERROR: AndroidManifest.xml not found. Run 'npx cap add android' first, "
        "from the project root."
    )

text = manifest.read_text(encoding="utf-8")

# Add Android TV / touchscreen feature declarations before <application>.
features = [
    '<uses-feature android:name="android.software.leanback" android:required="false" />',
    '<uses-feature android:name="android.hardware.touchscreen" android:required="false" />',
]
for feature in features:
    feature_name = re.search(r'android:name="([^"]+)"', feature).group(1)
    if feature_name not in text:
        match = re.search(r'(?m)^[ \t]*<application\b', text)
        if not match:
            sys.exit("ERROR: Could not find <application> in AndroidManifest.xml.")
        text = text[:match.start()] + "    " + feature + "\n" + text[match.start():]

# Allow HTTP IPTV servers when the user supplies an http:// Xtream host.
app_match = re.search(r'<application\b[^>]*>', text, flags=re.S)
if not app_match:
    sys.exit("ERROR: Could not find the <application> opening tag.")
app_tag = app_match.group(0)
if "android:usesCleartextTraffic" not in app_tag:
    updated = app_tag[:-1] + ' android:usesCleartextTraffic="true">'
    text = text[:app_match.start()] + updated + text[app_match.end():]

# Add Android TV launcher category to the activity that already has LAUNCHER.
launcher = re.search(
    r'<activity\b[^>]*>.*?</activity>',
    text,
    flags=re.S
)
if launcher and "android.intent.category.LEANBACK_LAUNCHER" not in launcher.group(0):
    block = launcher.group(0)
    category = re.search(
        r'<category\s+android:name="android\.intent\.category\.LAUNCHER"\s*/>',
        block
    )
    if category:
        addition = '\n                <category android:name="android.intent.category.LEANBACK_LAUNCHER" />'
        block = block[:category.end()] + addition + block[category.end():]
        text = text[:launcher.start()] + block + text[launcher.end():]
    else:
        print("WARNING: No LAUNCHER category found; TV launcher category was not added.")
elif not launcher:
    print("WARNING: No <activity> block found; TV launcher category was not added.")

manifest.write_text(text, encoding="utf-8")
print("OK: Android TV features and cleartext setting checked/applied.")

import re, sys
p = "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf-8").read()
if "leanback" in s:
    print("already patched"); sys.exit()
feat = ('    <uses-feature android:name="android.software.leanback" android:required="false" />\n'
        '    <uses-feature android:name="android.hardware.touchscreen" android:required="false" />\n\n    <application')
s = s.replace("<application", feat, 1)
s = s.replace('<category android:name="android.intent.category.LAUNCHER" />',
              '<category android:name="android.intent.category.LAUNCHER" />\n'
              '                <category android:name="android.intent.category.LEANBACK_LAUNCHER" />', 1)
s = s.replace("<application", '<application android:usesCleartextTraffic="true"', 1) if "usesCleartextTraffic" not in s else s
open(p, "w", encoding="utf-8").write(s)
print("patched: Android TV + cleartext enabled")

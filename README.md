# Mesut — بناء التطبيق (أندرويد / Android TV / آيفون)

## المتطلبات
- Node.js 18 أو أحدث
- Android Studio (يتضمن JDK 17)
- للآيفون: جهاز Mac مع Xcode

## أندرويد وAndroid TV
```
npm install
npx cap add android
python3 patch-tv.py
npx cap sync android
npx cap open android
```
في Android Studio: Build ← Build Bundle(s) / APK(s) ← Build APK(s).
ملف الـ APK يكون في android/app/build/outputs/apk/debug/

تثبيته على التلفاز: فعّل «خيارات المطور» ثم «تصحيح ADB»، ثم:
```
adb connect IP_التلفاز:5555
adb install app-debug.apk
```
أو انسخ الملف بفلاشة وثبّته بمدير ملفات.

## آيفون
```
npm install @capacitor/ios
npx cap add ios
npx cap sync ios
npx cap open ios
```
ثم شغّله من Xcode (النشر على App Store يحتاج حساب مطوّر).

## بعد تعديل الواجهة
عدّل www/index.html ثم `npx cap sync`.

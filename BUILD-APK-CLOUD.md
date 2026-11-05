# بناء Mesut IPTV بصيغة APK دون كمبيوتر

أضفنا GitHub Actions workflow في `.github/workflows/build-apk.yml` ليبني APK على خوادم GitHub.

## الخطوات من الهاتف
1. أنشئ مستودعاً جديداً على https://github.com/new (يمكن جعله Private).
2. ارفع جميع ملفات هذا المشروع إلى المستودع، مع مجلد `.github/workflows` وملف `build-apk.yml` بداخله.
3. افتح تبويب Actions في المستودع وفعّل Actions إذا طُلب منك ذلك.
4. شغّل `Build Mesut Android APK` عبر Run workflow، أو ادفع الملفات إلى فرع `main` أو `master`.
5. بعد نجاح العملية، افتح تشغيل workflow ثم نزّل Artifact باسم `mesut-iptv-debug-apk`.
6. فك ضغط الملف المنزّل وثبّت `app-debug.apk` على جهاز Android أو TV Box.

ملاحظات:
- هذه عملية بناء Debug وليست نسخة Release موقعة للنشر على المتجر.
- لم يُختبر التطبيق على جهاز فعلي.
- نجاح البناء لا يضمن أن كل خوادم IPTV أو صيغ الفيديو ستعمل؛ يلزم اختبارها على الجهاز.

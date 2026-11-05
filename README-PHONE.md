# بناء Mesut IPTV من هاتف Android فقط

## الطريقة الأسهل: GitHub Actions
- ارفع محتويات مجلد المشروع إلى جذر مستودعك، وليس المجلد الأب كله.
- افتح GitHub من المتصفح، ثم المستودع > Actions.
- اختر `Build Mesut Android APK` واضغط `Run workflow`.
- عند نجاح العملية افتح التشغيل ونزّل Artifact `mesut-iptv-debug-apk`.
- فك ملف ZIP وثبّت `app-debug.apk`.

## البناء محلياً (اختياري)
يتطلب Node.js وJava 17 وAndroid SDK وGradle، لذلك GitHub Actions أنسب إذا كنت تعمل من الهاتف فقط.

```bash
npm install
npx cap add android   # مرة واحدة فقط
python3 patch-tv.py
npx cap sync android
cd android && ./gradlew assembleDebug
```

استخدم فقط اشتراكات وروابط وقوائم تملك حق الوصول إليها. لا ترسل بيانات Xtream إلى أشخاص آخرين.

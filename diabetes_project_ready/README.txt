مشروع تدريب موديل السكري الرقمي
================================

الملفات:
- diabetes_training_ready.ipynb : دفتر التدريب الكامل، شغّل الخلايا بالترتيب.
- diabetes_binary_health_indicators_BRFSS2015.csv : ملف الداتا الأصلي.
- diabetes_model.joblib : الموديل المحفوظ مع أسماء الأعمدة والعتبة.
- requirements.txt : المكتبات المطلوبة.

التشغيل:
1. فك ضغط الملف ZIP.
2. افتح المجلد في VS Code.
3. ثبّت المكتبات من Terminal:
   python -m pip install -r requirements.txt
4. افتح diabetes_training_ready.ipynb واختر Python kernel.
5. شغّل الخلايا بالترتيب (Run All).

نتيجة التقييم المنفّذ أثناء تجهيز الحزمة:
- Recall class 0: 0.7479
- Recall class 1: 0.7488
- Accuracy: 0.7480
- Balanced accuracy: 0.7483
- Threshold المختار من Validation: 0.5447

مهم:
تم اختيار العتبة باستخدام Validation وليس Test. النتائج التجريبية التي ظهرت لم تحقق Recall أعلى من 90% للفئتين معاً. لا يصح الادعاء بذلك أو تغيير طريقة الاختبار للوصول إلى رقم شكلي.
هذا نموذج تعليمي على مؤشرات صحية، وليس تشخيصاً طبياً أو بديلاً عن الطبيب.

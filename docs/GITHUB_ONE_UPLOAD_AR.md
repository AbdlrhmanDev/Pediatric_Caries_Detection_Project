# طريقة استبدال ملفات GitHub دفعة واحدة — بدون فقدان التاريخ

**لا تحذف المستودع نفسه ولا ملف `.git` المحلي.** افتح GitHub Desktop، ثم Clone للمستودع الحالي. في مجلد النسخة المحلية احذف الملفات القديمة **ما عدا `.git` المخفي**. انسخ محتويات مجلد `Pediatric_Caries_Detection_Project` الذي جاء داخل ZIP إلى جذر النسخة المحلية، بحيث يكون `README.md` مباشرة في الجذر و`notebooks/` و`manifests/` و`results/` بجانبه. في GitHub Desktop تحقق من التغييرات ثم اكتب رسالة commit مثل `Replace fragmented revision artifacts with verified structured release`، واضغط `Commit to main` ثم `Push origin`. هذا دفع واحد لكامل التحديث، ويحفظ تاريخ المشروع.

بديل المتصفح: افتح المستودع واختر `Add file > Upload files`، اسحب **محتويات المجلد المستخرج** مع المجلدات الفرعية في عملية رفع واحدة، ثم `Commit changes`. انتبه: GitHub لا يفك ضغط ZIP المرفوع داخل المستودع. هذا البديل لا يحذف الملفات القديمة تلقائياً؛ إذا أردت تنظيفاً كاملاً استخدم GitHub Desktop.

بعد الرفع تأكد أن الملفات على الروابط:
- `README.md`
- `notebooks/Step_08D_Combined_33_Expert_Approved_GT_Sensitivity_Colab.ipynb`
- `results/step08d/official_validator_metrics.csv`
- `manifests/step08d_96_image_correction_manifest.csv`
- `data/README.md`

لا تنشر صور الأشعة أو سجل الأطباء الموقّع أو أرشيف التعليقات الخام ما لم تتأكد من ترخيص وإذن إعادة التوزيع. الأوزان غير مرفقة؛ انشرها فقط بإذن صحيح وببصمتها المحددة.

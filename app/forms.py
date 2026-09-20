from django import forms

class PreAuthForm(forms.Form):
    name = forms.CharField(label="الاسم", max_length=100)
    contact = forms.CharField(label="رقم الهاتف أو البريد الإلكتروني", max_length=100)
    service_type = forms.CharField(label="نوع الخدمة", max_length=100)
    description = forms.CharField(label="وصف الحالة", widget=forms.Textarea, required=False)
    file = forms.FileField(label="تحميل الملف", required=False)

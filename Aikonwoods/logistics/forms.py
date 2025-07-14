from django import forms
from django_recaptcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    company = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
   # captcha = ReCaptchaField()
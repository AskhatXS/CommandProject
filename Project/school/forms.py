from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django_recaptcha.fields import ReCaptchaField

from .models import Submission


class RegistrationForm(UserCreationForm):
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'captcha']


class LoginForm(forms.ModelForm):
    login = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username', 'password', 'captcha']


class GradeForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['grade', 'comments']
        labels = {
            'grade': 'Оценка',
            'comments': 'Комментарии'
        }
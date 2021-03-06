from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm

# ユーザー新規登録
class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ['username', 'email', 'password']
    
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


#ログインフォーム
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='', 
    widget=forms.TextInput(attrs={'placeholder': 'メールアドレス'}))
    password = forms.CharField(label='', 
    widget=forms.PasswordInput(attrs={'placeholder': 'パスワード'}))
    remember = forms.BooleanField(label='ログイン状態を保持する', required=False)
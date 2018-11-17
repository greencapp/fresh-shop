from django import forms

from user.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=5, required=True)
    password = forms.CharField(max_length=20, min_length=8, required=True)
    password2 = forms.CharField(max_length=20, min_length=8, required=True)
    email = forms.EmailField(required=True)

    def clean(self):
        # 获取用户名
        username = self.cleaned_data.get('username')
        # 校验用户是否注册
        user = User.objects.filter(username=username).first()
        if user:
            raise forms.ValidationError({'username': '该账户已注册, 请前往登录'})
        return self.cleaned_data


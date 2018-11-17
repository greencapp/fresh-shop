from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.forms import UserRegisterForm
from user.models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            password = make_password(form.cleaned_data.get('password'))
            # 实现注册
            User.objects.create(username=form.cleaned_data.get('username'),
                                password=password)
            return HttpResponseRedirect(reverse('user:login'))
        else:
            return render(request, 'register.html', {'errors': form.errors})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 验证完整性
        if not all([username, password]):
            msg = '用户名或密码必填'
            return render(request, 'login.html', {'msg': msg})
        # 验证用户
        user = User.objects.filter(username=username).first()
        if not user:
            msg = '该用户没有注册'
            return render(request, 'login.html', {'msg': msg})
        if check_password:
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('goods:index'))
    else:
        msg = '密码错误'
        return render(request, 'login.html', {'msg': msg})


def logout(request):
    if request.method == 'GET':
        del request.session['user_id']
        return HttpResponseRedirect(reverse('goods:index'))

# -*- conding:utf-8 -*-
# -*- conding:utf-8 -*-
from django import forms
from django.forms import widgets
from app01 import models

#用来校验字段并且渲染页面
class MyForm(forms.Form):
    #用户名
    username = forms.CharField(max_length=8,min_length=5,label='用户名',error_messages={
        'max_length':'用户名最大八位',
        'min_length':'用户名最小五位',
        'required':'用户名不能为空'
    #设置username框的样式
    },widget=widgets.TextInput(attrs={'class':'form-control'})
    )

    #密码
    password = forms.CharField(max_length=8,min_length=3,label='密码',error_messages={
        'max_length':'密码最大八位',
        'min_length':'密码最小三位',
        'required':'密码不能为空'
    #设置password框的样式
    },widget=widgets.PasswordInput(attrs={'class':'form-control'})
    )

    #确认密码
    confirm_password = forms.CharField(max_length=8, min_length=3, label='确认密码', error_messages={
        'max_length': '确认密码最大八位',
        'min_length': '确认密码最小三位',
        'required': '确认密码不能为空'
        # 设置password框的样式
    }, widget=widgets.PasswordInput(attrs={'class': 'form-control'})
                               )

    #邮箱
    email = forms.EmailField(label='邮箱',error_messages={
        'required':'邮箱不能为空',
        'invalid':'邮箱格式错误'
    },widget=widgets.EmailInput(attrs={'class': 'form-control'})
                             )

    #局部钩子  校验用户名是否存在
    #校验单个字段，就用clean_字段名
    def clean_username(self):
        #获取前面格式已经校验成功的username
        username = self.cleaned_data.get('username')
        #查询数据库中是否存在
        is_user = models.UserInfo.objects.filter(username=username)  #Queryset对象
        if is_user:
            self.add_error('username','用户已存在')  #如果存在，username框报的错误
        return username

    #全局钩子  校验两次密码是否输入一致
    #校验多个参数，就直接写clean
    def clean(self):
        #获取密码
        password = self.cleaned_data.get('password')
        #获取确认密码
        confirm_password = self.cleaned_data.get('confirm_password')
        if not password == confirm_password:
            self.add_error('confirm_password','两次密码输入不一致')
        return self.cleaned_data

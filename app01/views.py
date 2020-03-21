from django.shortcuts import render,redirect
from app01 import forms,models
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.utils.safestring import mark_safe
import dj_database_url
#登录
def login(request):
    if request.method == 'POST':
        back_dic = {'code': 100, 'msg': ''}
        username = request.POST.get('username')
        password = request.POST.get('password')
        #1.校验用户名和密码是否正确
        user_obj = auth.authenticate(username=username, password=password)
        if user_obj:
            #2.保存登录状态
            auth.login(request,user_obj)
            back_dic['msg'] = '登录成功'
            back_dic['url'] = '/home/'
        else:
            back_dic['code'] = 101
            back_dic['msg'] = '用户名或密码错误'

        return JsonResponse(back_dic)
    return render(request,'login.html')


#注册
def register(request):
    #创建一个form对象传给页面，做页面渲染（form组件不仅可以校验也可以渲染页面）
    form_obj=forms.MyForm()   #form_obj包含姓名，密码，确认密码，邮箱，所以到前端需要循环取出
    #接收前端传递的数据
    if request.method == 'POST':
        #设置给前端返回的消息
        back_dic={'code':100,'msg':''}
        #接收前端传递的数据，进行校验
        form_obj=forms.MyForm(request.POST)
        if form_obj.is_valid():  #判断是否校验成功
            # 获取四个输入框校验成功的数据
            clean_data = form_obj.cleaned_data  # clean_data = {'username':'','password':'','confirm_password':'','email':''}
            # 删掉数据库中不存在的字段,方便保存到数据库中
            clean_data.pop('confirm_password')
            # 手动获取用户头像对象
            user_file = request.FILES.get('myfile')
            if user_file:
                clean_data['avatar'] = user_file

            #数据校验成功添加到数据库
            models.UserInfo.objects.create_user(**clean_data)
            back_dic['msg'] = '注册成功'
            back_dic['url'] = '/login/'  # 用于注册成功之后跳转到登录页面
        else:
            back_dic['code'] = 101
            back_dic['msg'] = form_obj.errors
        return JsonResponse(back_dic)

    return render(request,'register.html',locals())

#主页面
def home(request):
    #展示主页面，查询出所有文章
    article_list=models.Article.objects.all()
    return render(request,'home.html',locals())

#退出登录
@login_required   #使用自带的装饰器设置必须登录才能退出
def logout(request):
    auth.logout(request)
    return redirect('/login/')

#页面详情
#文章详情页
def article_detail(request,username,article_id):
    # 先获取用户用户名 查看是否存在
    user_obj = models.UserInfo.objects.filter(username=username).first()
    if not user_obj:
        # 如果用户不存在 应该返回一个404页面
        return render(request, 'errors.html')
    # 根据文章id 查询出对应的文章 展示到前端 即可
    article_obj = models.Article.objects.filter(pk=article_id,user=user_obj.id).first()
    #获取当前文章所有评论
    comment_list = models.Comment.objects.filter(article=article_obj)
    return render(request, 'article_detail.html', locals())

from django.db import transaction
#评论功能
#前端传递数据：文章编号，评论内容
def comment(request):

    if request.is_ajax():
        back_dic = {'code':100,'msg':''}
        #用户登录之后才显示评论列表
        if request.user.is_authenticated():
            content = request.POST.get('content')
            article_id = request.POST.get('article_id')
            # print(article_id,type(article_id))
            #如果是根评论就没有值
            parentId = request.POST.get('parentId')
            # print(parentId,type(parentId))
            #评论表和文章表中的评论字段数据要同步，用事务来做
            with transaction.atomic():
                models.Comment.objects.create(user=request.user,article_id=article_id,content=content,parent_id=parentId)
                models.Article.objects.filter(pk=article_id).update(comment_num=F('comment_num')+1)
            back_dic['msg'] = '评论成功'

        else:
            back_dic['code']=101
            back_dic['msg'] = mark_safe('请先<a href="/login/">登录</a>')  #取消转义
        return JsonResponse(back_dic)



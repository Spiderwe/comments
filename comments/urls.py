"""comments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
from django.views.static import serve
from comments import settings
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    #登录
    url(r'^login/', views.login),
    #注册
    url(r'^register/', views.register),
    #主页
    url(r'^home/', views.home),
    #退出登录
    url(r'^logout/', views.logout),
    # 文章评论功能
    url(r'^comment/', views.comment),
    # 手动暴露后端文件夹资源
    url(r'^media/(?P<path>.*)',serve,{"document_root":settings.MEDIA_ROOT}),
    # 文章详情页
    url(r'^(?P<username>\w+)/article/(?P<article_id>\d+)/', views.article_detail),

]

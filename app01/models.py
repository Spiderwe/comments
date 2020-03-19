from django.db import models

from django.contrib.auth.models import AbstractUser

#用户表  继承AbstractUser
class UserInfo(AbstractUser):
    #电话/用户名
    phone = models.BigIntegerField(null=True,blank=True)  #blank是用来告诉admin后台该字段可以不用填
    #头像,保存头像文件路径，用户上传的头像自动保存到avatar文件夹下
    avatar = models.FileField(upload_to='avatar/',default='avatar/default.jpg')  #没有设置就用默认路径的图片
    #创建时间
    create_time = models.DateField(auto_now_add=True)
    #允许为空，可能新创建的用户没有建站点
    # blog = models.OneToOneField(to='Blog',null=True)

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.username

#文章表
class Article(models.Model):
    #文章标题
    title = models.CharField(max_length=255)
    #文章摘要
    desc = models.CharField(max_length=255)
    #文章内容
    content = models.TextField()
    #创建时间
    create_time = models.DateField(auto_now_add=True)

    #普通字段
    #评论数
    comment_num = models.IntegerField(default=0)
    #点赞数
    up_num = models.IntegerField(default=0)
    #点踩数
    down_num = models.IntegerField(default=0)

    #外键
    user = models.ForeignKey(to='UserInfo',null=True)
    # tag = models.ManyToManyField(to='Tag',through='Article2Tag',through_fields=('article','tag'))
    # category = models.ForeignKey(to='Category',null=True)

    class Meta:
        verbose_name_plural = '文章表'

    def __str__(self):
        return self.title

# #点赞点踩表
# class UpAndDown(models.Model):
#     #对应用户
#     user = models.ForeignKey(to='UserInfo')
#     #对应文章
#     article = models.ForeignKey(to='Article')
#     #点赞还是点踩
#     is_up = models.BooleanField()  #传布尔值   存0/1
#
#     class Meta:
#         verbose_name_plural = '点赞点踩表'


#评论表
class Comment(models.Model):
    #对应用户评论
    user = models.ForeignKey(to='UserInfo')
    #对应文章
    article = models.ForeignKey(to='Article')
    #评论内容
    content = models.CharField(max_length=255)
    #创建时间
    create_time = models.DateField(auto_now_add=True)
    #父评论  和本表自己绑定，允许为空
    parent = models.ForeignKey(to='self',null=True)

    class Meta:
        verbose_name_plural = '评论表'
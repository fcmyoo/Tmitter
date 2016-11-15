"""Tmitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.template.context_processors import static

from mvc import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 主页
    url(r'^$', views.index),
    # 以P开头以一个或者多个数字结尾的消息发布页面分页
    url(r'^p/(?P<page_index>\d+)/$', views.index_page),
    # 查看登陆用户
    url(r'^user/$', views.index_user_self),
    # 查看指定用户的分页
    url(r'^user/(?P<username>[a-zA-Z\-_\d]+)/$', views.index_user),
    #  查看指定用户的分页
    url(r'^user/(?P<username>[a-zA-Z\-_\d]+)/(?P<page_index>\d+)/$', views.index_user_page),
    # 查看所有用户.朋友
    url(r'^users/$', views.users_index),
    # 登陆
    url(r'^signin/$', views.sigNin),
    # 登出
    url(r'^signout/$', views.signOut),
    # 注册
    url(r'^signup/$', views.signup),
    # 修改登陆用户信息
    url(r'^settings/$', views.settings),
    # 消息详情页
    url(r'^message/(?P<id>\d+)/$', views.detail),
    # 删除单条消息
    url(r'^message/(?P<id>\d+)/delete/$', views.detail_delete),
    # 添加朋友
    url(r'^friend/add/(?P<username>[a-zA-Z\-_\d]+)', views.friend_add),
    # 删除朋友
    url(r'^friend/remove/(?P<username>[a-zA-Z\-_\d]+)', views.friend_remove),
    # 发布消息
    url(r'^api/note/add/', views.api_note_add),

]

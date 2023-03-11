"""GraduateWorkP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from CommunityHospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path转换器
    # path('page/<int : page>', views.page_view)
    path('page/<int:page>', views.page_view),
    # """"
    # get到的教训：path转换器中：<int:page>里面居然不能使用空格分割开来，我还以为会转义出错，
    # """
    # 普通测试界面
    # path('test_html',views.test_html)
    #http:127.0.0.1:8000/整数/操作符/整数
    #path('<int:x>/<str:op>/<int:y>',views.cal_view),
    #正则表达式
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$',views.cal_view2)   #正则表达式匹配x op y
]

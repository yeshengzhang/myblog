"""myblob URL Configuration

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

from app import views as av

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^base/$', av.base),
    url(r'^$', av.index),
    url(r'^index/$', av.index),
    url(r'^read/$', av.read),
    url(r'^write/$', av.write),
    url(r'^login/$', av.login),
    url(r'^register/$', av.register),
    url(r'^logout/$', av.logout),
    url(r'^liuyan/$', av.liuyan),
    url(r'^about/$', av.about),
    url(r'^add_zan/$', av.add_zan),
]

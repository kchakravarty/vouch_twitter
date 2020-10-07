"""twitter_login URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from login_page import views as v
from login_page.utils import *
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',v.home,name='home'),
    url(r'^auth/$',v.auth,name='authentication'),
    url(r'^callback/$',v.callback,name='callback'),
    url(r'^check/$',v.check,name='check'),
    url(r'^login/',v.login,name='login'),
    url(r'^check/info', v.info,name='info'),
    url(r'^check/tweets',v.tweets,name='tweets'),
    url(r'^check/domain',v.domain,name='domain'),
    url(r'^logout/',auth_views.LogoutView.as_view(), name='logout'),

]

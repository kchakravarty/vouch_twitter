from django.conf.urls import url,include
from .views import *

urlpatterns = [

    url('',home,name='home_page'),

]

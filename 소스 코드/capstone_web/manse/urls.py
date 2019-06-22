from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('result/', views.result, name='result'),
    url(r'^$', views.main_page, name='main_page'),
]
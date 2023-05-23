from django.contrib import admin
from django.urls import path, include
from django_ads_app import views

urlpatterns = [
    path('', views.ret_str),

    path('txt/', views.read_txt),

    path('json/', views.ret_json),

    path('json_file/', views.ret_json_file),

    path('xl_file/', views.ret_xl_file),

    path('home/', views.ret_html)
]

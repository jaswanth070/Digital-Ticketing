
from django.contrib import admin
from django.urls import path
import users.views as views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home,name="home"),
]

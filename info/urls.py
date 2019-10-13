from django.contrib import admin
from django.urls import path
from . import views

app_name= 'info'
urlpatterns = [
    path('', views.homepage.as_view(), name='homepage'),
]

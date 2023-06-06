from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.optional, name='optional'),
    path('<str:name>',views.optional, name='optional'),
]
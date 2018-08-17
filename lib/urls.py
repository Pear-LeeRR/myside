#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.urls import path
from . import views

# 命名空间
app_name = 'lib'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('addBook/', views.addBook, name='addBook'),
    path('delBook/<int:book_id>', views.delBook, name='delBook'),
]

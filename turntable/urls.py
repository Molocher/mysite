#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 13:31
# @Author  : 作者名
# @File    : urls.py
# Version: 1.0
# @Project : mysite
# License: MIT

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from turntable import views

routers = DefaultRouter()
routers.register(r'manager', views.TurntableViewSets, basename='turntable')

urlpatterns = [
    path('', include(routers.urls)),
    path('condition', views.ActivityConditionView.as_view())
]

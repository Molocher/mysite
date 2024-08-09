#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 09:58
# @Author  : 作者名
# @File    : urls.py
# Version: 1.0
# @Project : mysite
# License: MIT

# from django.urls import path
# from snippets import views
# from snippets.views import SnippetViewSet, UserViewSet
# from rest_framework import renderers
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderers_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = [
#     # path('snippets/', views.snippets_list),
#     # path('snippets/<int:pk>/', views.snippet_detail),
#     path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
#     path('', views.api_root),
#     path('snippets/<int:pk>/highlight', views.SnippetHighlight.as_view(), 'snippet-highlight')
# ]

# urlpatterns = [
#     path('', views.api_root),
#     path('snippets/', snippet_list, name='snippet_list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet_detail'),
#     path('snippets/<int:pk>/highlight', snippet_highlight, name='snippet-highlight'),
#     path('/users/', user_list, name='user-list'),
#     path('/users/<int:pk>/', user_detail, name='user-detail')
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 13:54
# @Author  : 作者名
# @File    : permissions.py
# Version: 1.0
# @Project : mysite
# License: MIT

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

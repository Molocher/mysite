#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 13:15
# @Author  : 作者名
# @File    : serializers.py
# Version: 1.0
# @Project : mysite
# License: MIT

from rest_framework import serializers
from turntable.models import TurnTableModel, ActivityConditionModel


class TurnTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnTableModel
        fields = "__all__"


class TurnTableUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnTableModel
        fields = ['id', 'status', 'share_language']


class ActivityConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityConditionModel
        fields = "__all__"

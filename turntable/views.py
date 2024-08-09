from decimal import Decimal

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from turntable.result import success, error
from turntable.models import TurnTableModel, ActivityConditionModel
from turntable.serializers import TurnTableSerializer, TurnTableUpdateSerializer, ActivityConditionSerializer


# Create your views here.

class MyPermissions(BasePermission):
    message = "Token Required"

    def has_permission(self, request, view):
        print(request)
        return False


class TurntableViewSets(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = TurnTableModel.objects.all()

    # permission_classes = [MyPermissions]

    def get_serializer_class(self):
        if self.action == 'update':
            return TurnTableUpdateSerializer
        else:
            return TurnTableSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='page_size'
            ),
            OpenApiParameter(
                name='page_num'
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('page_size', 20)
        if page_size == "":
            page_size = 20
        else:
            page_size = int(page_size)
        page_num = request.GET.get('page_num', 1)
        if page_num == "":
            page_num = 1
        else:
            page_num = int(page_num)
        query_set = self.filter_queryset(self.get_queryset())
        total_num = len(list(query_set))
        paginator = Paginator(query_set, page_size)
        try:
            page = paginator.page(page_num)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        serializer = self.get_serializer(page, many=True)
        data = {
            "records": serializer.data,
            "page_size": page_size,
            "page_num": page_num,
            "total_num": total_num
        }
        return success(data=data)

    def create(self, request, *args, **kwargs):
        data = request.data
        # check params
        # blocks_number >= 3 and blocks_number <=20
        if data['blocks_number'] < 3 or data['blocks_number'] > 20:
            return error(msg='转盘区块数量在3到20之间')
        # 计算设置中的权重和要等于100
        turntable_setting = data['turntable_setting']
        weights = Decimal("0")
        for item in turntable_setting:
            weights += Decimal(item['weights'])
        if Decimal("100").compare(weights) != 0:
            return error(msg='转盘各区块权重和为100')
        super().create(request, *args, **kwargs)
        return success(msg='创建活动成功')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return success(data=serializer.data)

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return success()

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return success()

    @action(detail=False, methods=['get'], url_path='activitys')
    def get_activity_name_list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.values('id', 'activity_name')
        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(list(queryset))
        return Response(list(queryset))


class ActivityConditionView(APIView):
    def get(self, request, format=None):
        queryset = ActivityConditionModel.objects.all()
        serializer = ActivityConditionSerializer(queryset, many=True)
        return Response(serializer.data)

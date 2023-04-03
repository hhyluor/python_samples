# -*- coding: utf-8 -*-
# @Time : 2023/3/25 22:43
# @Author : hehaiyang
# @File : mixins.py
# @Project : django_samples
# @Function :
from django.db import connection
from django.db.models.query import QuerySet
from rest_framework import serializers


from django.db.models import Aggregate, CharField


class SerializerMixin:
    def get_serializer_class(self):
        """
        让 ViewSet 支持以下写法，而不是serializer_class（这段代码来自 jumpserver 源码
        serializer_classes = {
            'default': serializers.AssetUserWriteSerializer,
            'list': serializers.AssetUserReadSerializer,
            'retrieve': serializers.AssetUserReadSerializer,
        }
        """
        serializer_class = None
        if hasattr(self, 'serializer_classes') and isinstance(self.serializer_classes, dict):
            serializer_class = self.serializer_classes.get(self.action, self.serializer_classes.get('default'))
        if serializer_class:
            return serializer_class
        return super().get_serializer_class()

    def get_request_serializer(self, *args, **kwargs) -> serializers.Serializer:
        """
        校验请求数据并返回请求serializer
        """
        if 'data' not in kwargs:
            kwargs['data'] = self.request.data
        serializer = self.get_serializer(*args, **kwargs)
        serializer.is_valid(raise_exception=True)
        return serializer


class QuerySetMixin:
    def get_queryset(self):
        """
        Get the list of items for this view.
        This must be an iterable, and may be a queryset.
        Defaults to using `self.queryset`.

        This method should always be used rather than accessing `self.queryset`
        directly, as `self.queryset` gets evaluated only once, and those results
        are cached for all subsequent requests.

        You may want to override this if you need to provide different
        querysets depending on the incoming request.

        (Eg. return a list of items that is specific to the user)
        """
        # assert self.queryset is not None, (
        #         "'%s' should either include a `queryset` attribute, "
        #         "or override the `get_queryset()` method."
        #         % self.__class__.__name__
        # )

        queryset = None
        if hasattr(self, 'queryset_es') and isinstance(self.queryset_es, dict):
            queryset = self.queryset_es.get(self.action, self.queryset_es.get('default'))
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset


class GroupConcat(Aggregate):
    """自定义GroupConcat数据库查询"""
    function = 'GROUP_CONCAT'
    substring_length = 1024 * 4
    template = '%(function)s(%(distinct)s%(expressions)s%(ordering)s%(separator)s)'

    def __init__(self, expression, distinct=False, ordering=None, separator=',', **extra):
        with connection.cursor() as cursor:
            cursor.execute(f'SET SESSION group_concat_max_len = {self.substring_length}')
        super(GroupConcat, self).__init__(
            expression,
            distinct='DISTINCT ' if distinct else '',
            ordering=' ORDER BY %s' % ordering if ordering is not None else '',
            separator=' SEPARATOR "%s"' % separator,
            output_field=CharField(),
            **extra
        )
# -*- coding: utf-8 -*-
# @Time : 2023/3/25 22:43
# @Author : hehaiyang
# @File : pagination.py
# @Project : django_samples
# @Function :
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from collections import OrderedDict

from utils.response import CommonResponse, CommonStatus


class CustomNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class CodePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return CommonResponse(data=OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]), status=CommonStatus.OK)


# 分页器  2023-02-06后弃用
class PagePagination(PageNumberPagination):
    """自定义分页器，查第n页，每页显示n条数据，2023-02-06后弃用，统一使用上面的分页器"""
    # URL中页码的参数
    page_query_param = "page"
    # URL参数中每页显示条数的参数
    page_size_query_param = "pageSize"
    # 指定每页显示多少条数据
    page_size = 10
    # 每页最多显示多少条数据
    max_page_size = 100

    def get_paginated_response(self, data, code=2000):
        return Response(OrderedDict([
            ("code", code),
            ("count", self.page.paginator.count),
            ("next", self.get_next_link()),
            ("previous", self.get_previous_link()),
            ("data", data)
        ]))

# -*- coding: utf-8 -*-
# @Time : 2023/3/25 22:44
# @Author : hehaiyang
# @File : response.py
# @Project : django_samples
# @Function :
from enum import Enum

from rest_framework.response import Response


class CommonStatus(Enum):
    OK = (2000, '请求成功')
    CREATED = (2001, '创建成功')
    DELETE = (2004, '删除成功')
    PARAM_ERROR = (4000, '参数错误')
    UPDATA_ERROR = (4002, '修改失败')
    UNAUTHORIZED = (4001, '未授权或验证失败')
    FORBIDDEN = (4003, '权限不允许')
    CONFIRM = (4004, '待确认')
    DATA_NOT_FOUND = (4005, '未查找到数据')
    DELETE_ERROR = (4006, '删除失败')
    ADD_ERROR = (4007, '增加失败')
    SERVER_INNER_ERROR = (5000, '服务端内部错误')
    SERVICE_UNAVAILABLE = (5003, '服务端拒接服务')


class CommonResponse(Response):
    def __init__(self, status: CommonStatus = CommonStatus.OK, data=None, message: str = None,
                 result_dict: dict = None, *args, **kwargs):
        result = dict(zip(('code', 'message'), status.value))
        if message:
            result['message'] = message
        # 空数组情况不能忽略
        if data is not None:
            result['data'] = data
        # 给机构外层添加其他键值对
        if result_dict is not None:
            result.update(result_dict)
        if kwargs.get("status_code") is not None:
            kwargs["status"] = kwargs["status_code"]
            del kwargs["status_code"]
        super().__init__(*args, data=result, **kwargs)

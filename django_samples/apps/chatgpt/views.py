# Create your views here.

import datetime

from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from utils.mixins import SerializerMixin, QuerySetMixin
from utils.pagination import CodePagination
from utils.response import CommonResponse, CommonStatus
from .tasks import add_1
from tasks import add


class ChatGPTViews(SerializerMixin, QuerySetMixin, GenericViewSet):
    pagination_class = CodePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = None

    @action(detail=False, methods=["POST"], url_path="samples")
    def get_samples(self, request, *args, **kwargs):
        n = int(request.data.get("n", 1))
        m = int(request.data.get("m", 1))
        run_at = timezone.now() + datetime.timedelta(seconds=5)
        add.delay(n, m)
        add.apply_async(args=(n, m), eta=run_at)
        return CommonResponse(status=CommonStatus.OK, data="sum")

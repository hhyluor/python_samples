from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.chatgpt.views import ChatGPTViews

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("chatgpt", ChatGPTViews, basename="chatgpt")

urlpatterns = [
    path("", include(router.urls)),

]

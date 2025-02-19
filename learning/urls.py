from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import learnViewSet

router = routers.DefaultRouter()
router.register(r'learns',learnViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from cryptalme import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'alerts', views.AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pub/', views.index, name="index"),
    path('sub/', views.listen, name="sub"),
]

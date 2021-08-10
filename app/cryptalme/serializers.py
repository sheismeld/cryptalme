from rest_framework import serializers

from cryptalme.adapters.django_storage import DjangoStorage
from cryptalme.entities.alert import Alert
from cryptalme.models import UserModel, AlertModel
from cryptalme.use_cases.alert_use_cases import AlertUseCase


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name', 'email']


class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlertModel
        fields = ['id', 'stop_price', 'alert_type', ]

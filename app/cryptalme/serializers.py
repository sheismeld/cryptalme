from rest_framework import serializers

from cryptalme.entities.alert import Alert
from cryptalme.models import UserModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name', 'email']


class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'stop_price', 'alert_type',]

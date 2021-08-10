from django.http import HttpResponse

# Create your views here.


from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from cryptalme.adapters.django_storage import DjangoStorage
from cryptalme.serializers import UserSerializer, AlertSerializer
from cryptalme.models import UserModel, AlertModel
from cryptalme.use_cases.alert_use_cases import AlertUseCase
from cryptalme.use_cases.user_use_cases import UserUseCase
import time
from redis import StrictRedis

from cryptalme.adapters.alert_console_handler import AlertSubscriber, RedisCache, RedisPubSubHandler
from cryptalme.entities.alert import Alert


def index(request):
    return HttpResponse('ok')


def listen(request):
    redis_instance = RedisCache.get_instance()
    print(redis_instance)

    for i in range(38000, 38200):
        handler = RedisPubSubHandler(instance=redis_instance)
        alert = Alert(stop_price=i, alert_type="UNDER", alert_id=1, user=None,)
        sub = AlertSubscriber(alert=alert, handler=handler)
        sub.register()
    return HttpResponse('sub ok')


class AlertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AlertModel.objects.all().order_by('-created_at')
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserModel.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(**kwargs)
    #     self.usecases: UserUseCase = UserUseCase(DjangoStorage())
    #
    # def list(self, request, *args, **kwargs):
    #     serializer = UserSerializer(UserModel.objects.all(), many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     serializer = UserSerializer(UserModel.objects.all(), many=True)
    #     print(request.__str__())
    #     return Response(serializer.data)


class UserList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        return Response({})

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

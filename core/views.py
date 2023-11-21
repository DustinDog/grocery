from core.models import User
from core.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView


class UserCreateViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
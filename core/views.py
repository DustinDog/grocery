from core.models import User
from core.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView
from django.core.cache import cache

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

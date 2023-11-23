from core.models import User
from core.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from django.core.cache import cache

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    cache_key = "user_viewset"


    def get_queryset(self):
        queryset = cache.get(self.cache_key)

        if queryset is None:
            queryset = User.objects.all()
            cache.set(self.cache_key, queryset)
        return queryset
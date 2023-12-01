from django.urls import path, include
from core.views import UserCreate, UserList

urlpatterns = [
    path("create/", UserCreate.as_view(), name="create_user"),
    path("user_list/", UserList.as_view(), name="user_list"),
    ]
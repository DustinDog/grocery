from django.urls import path, include
from core.views import UserCreate, UserViewSet

urlpatterns = [
    path("create/", UserCreate.as_view(), name="create_user"),
    path("user_viewset/", UserViewSet.as_view({"get": "list"}), name="user_viewset"),
    path(
        "user_viewset/<int:pk>/",
        UserViewSet.as_view({"get": "retrieve"}),
        name="user_viewset",
    ),
]
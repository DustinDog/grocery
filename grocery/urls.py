from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from core.views import UserViewSet


router = routers.DefaultRouter()
router.register(r"user_viewset", UserViewSet)

urlpatterns = [
    path("api/", include("core.urls")),

    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",
    ),
]

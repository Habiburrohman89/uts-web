from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PemesananViewSet
router = DefaultRouter()
router.register(r'pemesanan',PemesananViewSet)

urlpatterns = [
    path('pemesanan/', include(router.urls)),
]
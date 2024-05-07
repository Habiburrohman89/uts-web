from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PembayaranViewSet

router = DefaultRouter()
router.register(r'pembayaran', PembayaranViewSet)

urlpatterns = [
    path('pembayaran/', include(router.urls)),
]

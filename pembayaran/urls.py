from django.urls import path
from .import views

urlpatterns = [
    path('pembayaran/', views.pembayaran_list),
]
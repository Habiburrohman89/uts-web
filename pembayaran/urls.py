from django.urls import path, include
from pembayaran import views



urlpatterns = [
    path('pembayaran/',views.pembayaran_list),
    path('pembayaran/<int:pk>/', views.pembayaran_detail),
]

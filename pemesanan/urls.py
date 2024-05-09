from django.urls import path, include
from  .import views


urlpatterns = [
    path('pemesanan/',views.PemesananList.as_view()),
    path('pemesanan/<int:pk>/', views.PemesananDetail.as_view()),
]
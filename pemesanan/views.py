from rest_framework import viewsets
from .models import Penyewaan
from .serializers import pemesananserializers


class PemesananViewSet(viewsets.ModelViewSet):
    queryset = Penyewaan.objects.all()
    serializer_class = pemesananserializers

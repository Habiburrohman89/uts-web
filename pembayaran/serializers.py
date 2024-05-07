from rest_framework import serializers
from .models import Pembayaran

class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = '__all__'

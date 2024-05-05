from rest_framework import serializers
from .models import pembayaran

class PembayaranSerializers(serializers.ModelSerializer):
    class Meta:
        model = pembayaran
        fields = ['id', 'nama','berpa_hari', 'harga']
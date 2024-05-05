from rest_framework import serializers
from .models import Penyewaan

class pemesananserializers(serializers.ModelSerializer):
    class Meta:
        model = Penyewaan
        fields = '__all__'
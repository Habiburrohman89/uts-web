from .models import Penyewaan
from .serializers import pemesananserializers
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions



class PemesananList(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        pemesanan = Penyewaan.objects.all()
        serializer = pemesananserializers(pemesanan, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = pemesananserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PemesananDetail(APIView):
    permission_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Penyewaan.objects.get(pk=pk)
        except Penyewaan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        penyewaan = self.get_object(pk)
        serializer = pemesananserializers(penyewaan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        penyewaan = self.get_object(pk)
        serializer = pemesananserializers(penyewaan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        penyewaan = self.get_object(pk)
        penyewaan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


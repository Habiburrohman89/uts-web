from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pembayaran
from .serializers import PembayaranSerializer


@api_view(['GET', 'POST'])
def pembayaran_list(request,format=None):
    if request.method == 'GET':
        pembayaran = Pembayaran.objects.all()
        serializer = PembayaranSerializer(pembayaran, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PembayaranSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def pembayaran_detail(request, pk, format=None):
    try:
        pembayaran = Pembayaran.objects.get(pk=pk)
    except Pembayaran.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PembayaranSerializer(pembayaran)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PembayaranSerializer(pembayaran, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pembayaran.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
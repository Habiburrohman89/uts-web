from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import pembayaran
from .serializers import PembayaranSerializers

@csrf_exempt
def pembayaran_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        pembayarans = pembayaran.objects.all()
        serializer = PembayaranSerializers(pembayarans, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PembayaranSerializersr(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

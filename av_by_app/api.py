from rest_framework import viewsets, permissions
from .models import Ad
from .serializers import AdSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Определяем представление для работы с объявлениями (обрабатываем запросы для операций над объявлениями о продаже автомобилей)
class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AdSerializer



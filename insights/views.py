from rest_framework import viewsets
from .models import Plant, WeeklyLoss
from .serializers import PlantSerializer, WeeklyLossSerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class WeeklyLossViewSet(viewsets.ModelViewSet):
    queryset = WeeklyLoss.objects.all()
    serializer_class = WeeklyLossSerializer

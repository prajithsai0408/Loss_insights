from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlantViewSet, WeeklyLossViewSet

router = DefaultRouter()
router.register(r'plants', PlantViewSet)
router.register(r'weeklyloss', WeeklyLossViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

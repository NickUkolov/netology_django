from django.urls import path
from .views import SensorsView, MeasurementView, OneSensorView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensor/<pk>/', OneSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]

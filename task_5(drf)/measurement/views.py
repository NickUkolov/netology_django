from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        name = self.request.data.get('name')
        description = self.request.data.get('description')

        return serializer.save(
            name=name,
            description=description
        )


class OneSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_update(self, serializer):
        name = self.request.data.get('name')
        description = self.request.data.get('description')

        return serializer.save(
            name=name,
            description=description
        )


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor = self.request.data.get('sensor_id')
        sensor_id = Sensor.objects.get(id=sensor)
        temperature = self.request.data.get('temperature')

        return serializer.save(
            sensor_id=sensor_id,
            temperature=temperature,
        )

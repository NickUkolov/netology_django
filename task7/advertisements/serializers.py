from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["creator"] = user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context['request'].user
        objects = Advertisement.objects.filter(status='OPEN', creator=user)
        method = self.context['request'].method
        status = self.initial_data.get('status')

        if len(objects) >= 10 and method == 'POST' and not status or status == 'OPEN':
            raise ValidationError('Превышено количество открытых объявлений')
        if len(objects) >= 10 and status == 'OPEN' and method == 'PATCH':
            raise ValidationError('Превышено количество открытых объявлений')
        return data

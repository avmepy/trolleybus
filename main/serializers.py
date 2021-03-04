from rest_framework import serializers

from main.models import Trolleybus


class TrolleybusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trolleybus
        fields = '__all__'

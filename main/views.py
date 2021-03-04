from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response

from main.models import Trolleybus
from main.serializers import TrolleybusSerializer


class TrolleybusView(views.APIView):
    def get(self, request, trolleybus_id):
        print(trolleybus_id)
        trolleybus = Trolleybus.objects.filter(pk=trolleybus_id)

        if trolleybus:
            serializer = TrolleybusSerializer(trolleybus.first())

            return serializer.data
        return Response({'bad': 'bad'})

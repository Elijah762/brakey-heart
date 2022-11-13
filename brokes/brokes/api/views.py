from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import BrakeData

from .serializers import PiDataSerializer, BrakeDataSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@csrf_exempt
def sendData(request):
    serializer = PiDataSerializer(data=request.data)

    if serializer.is_valid():
        try:
            serializer.save(x_acc=request.x_acc, y_acc=request.y_acc, z_acc=request.z_acc)
            return Response("Win", status=status.HTTP_201_CREATED)

        except Exception:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    return Response("else", status=status.HTTP_400_BAD_REQUEST)


class BrakeDataListView(APIView):
  def get(self, request, format=None):
    brake_data = BrakeData.objects.latest('ts')
    serializer = BrakeDataSerializer(brake_data)
    return Response(serializer.data)

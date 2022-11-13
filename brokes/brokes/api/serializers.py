from rest_framework import serializers
from .models import BrakeData, PiData


class BrakeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrakeData
        fields = '__all__'


class PiDataSerializer(serializers.ModelSerializer):
    x_acc = serializers.DecimalField(decimal_places=2, max_digits=5)
    y_acc = serializers.DecimalField(decimal_places=2, max_digits=5)
    z_acc = serializers.DecimalField(decimal_places=2, max_digits=5)

    class Meta:
        model = PiData
        fields = [

        ]

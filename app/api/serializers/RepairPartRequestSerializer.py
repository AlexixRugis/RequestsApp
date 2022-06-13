from rest_framework import serializers
from .RepairPartSerializer import RepairPartSerializer

from app.models.parts.RepairPartRequest import RepairPartRequest

class RepairPartRequestSerializer(serializers.ModelSerializer):
    part = RepairPartSerializer()

    class Meta:
        model = RepairPartRequest
        fields = '__all__'
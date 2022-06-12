from rest_framework import serializers
from app.models.parts.RepairPart import *


class RepairPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairPart
        fields = '__all__'
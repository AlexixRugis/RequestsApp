from rest_framework import serializers
from app.models.repair_requests.RepairRequest import *

class RepairRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairRequest
        fields = '__all__'
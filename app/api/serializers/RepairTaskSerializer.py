from flask import request
from rest_framework import serializers
from app.api.serializers.RepairPartRequestSerializer import RepairPartRequestSerializer
from app.models.repair_requests.RepairTask import *
from .RepairRequestSerializer import *
from .EmployeeSerializer import *

class RepairTaskSerializer(serializers.ModelSerializer):
    request = RepairRequestSerializer()
    executor = EmployeeSerializer()
    parts = RepairPartRequestSerializer(many=True)

    class Meta:
        model = RepairTask
        fields = '__all__'
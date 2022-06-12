from flask import request
from rest_framework import serializers
from app.models.repair_requests.RepairTask import *
from .RepairRequestSerializer import *
from .EmployeeSerializer import *

class RepairTaskSerializer(serializers.ModelSerializer):
    request = RepairRequestSerializer()
    executor = EmployeeSerializer()

    class Meta:
        model = RepairTask
        fields = '__all__'
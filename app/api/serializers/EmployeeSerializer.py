from rest_framework import serializers
from app.models.employees.Employee import *
from .PostSerializer import *

class EmployeeSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Employee
        fields = ('name', 'phone_number', 'email', 'post',)
from rest_framework import serializers
from app.models.parts.PartCategory import *

class PartCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartCategory
        fields = '__all__'
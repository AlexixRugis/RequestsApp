from rest_framework import serializers
from app.models.employees.Post import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
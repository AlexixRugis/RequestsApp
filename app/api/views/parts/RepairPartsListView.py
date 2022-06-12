from rest_framework import generics
from app.api.serializers.RepairPartSerializer import RepairPartSerializer
from app.models.parts.RepairPart import RepairPart

class RepairPartsListView(generics.ListAPIView):
    serializer_class = RepairPartSerializer

    search_fields = ('name',)

    def get_queryset(self):
        return RepairPart.objects.all()
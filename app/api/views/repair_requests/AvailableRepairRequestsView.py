from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.api.serializers.RepairRequestSerializer import RepairRequestSerializer
from app.services.RepairRequestsService import RepairRequestsService

class AvailableRepairRequestsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = RepairRequestSerializer

    search_fields = ('name', 'description', 'org_name', )

    def get_queryset(self):
        return RepairRequestsService.get_available_requests()
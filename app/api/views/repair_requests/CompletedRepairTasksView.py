from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.api.serializers.RepairTaskSerializer import RepairTaskSerializer
from app.services.RepairTasksService import RepairTasksService

class CompletedRepairTasksView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RepairTaskSerializer

    search_fields = ('request__name', 'request__description', 'request__org_name')

    def get_queryset(self):
        return RepairTasksService.get_completed_tasks(self.request)
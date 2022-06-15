from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.api.serializers.RepairTaskSerializer import RepairTaskSerializer
from app.services.RepairTasksService import RepairTasksService

class CompletedRepairTaskDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = RepairTaskSerializer
    
    def get_queryset(self):
        return RepairTasksService.get_completed_tasks(self.request)
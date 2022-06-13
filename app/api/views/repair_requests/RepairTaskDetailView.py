from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.api.serializers.RepairTaskSerializer import RepairTaskSerializer
from app.services.RepairTasksService import RepairTasksService

class RepairTaskDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = RepairTaskSerializer
    
    def get_queryset(self):
        return RepairTasksService.get_account_tasks(self.request)
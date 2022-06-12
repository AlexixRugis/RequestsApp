from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.api.serializers.RepairTaskSerializer import RepairTaskSerializer
from app.services.RepairTasksManager import RepairTasksManager

class AccountRepairTasksView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RepairTaskSerializer

    search_fields = ('request__name', 'request__description', 'request__org_name')

    def get_queryset(self):
        return RepairTasksManager.get_account_tasks(self.request)
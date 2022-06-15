from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from app.models.repair_requests.RepairTask import *
from app.services.RepairTasksService import RepairTasksService

class CompleteTaskView(views.APIView):
    permission_classes = (IsAuthenticated, )
    http_method = 'POST'

    def post(self, request, pk):
        task = get_object_or_404(RepairTask, pk=pk)
        s = RepairTasksService.complete_task(request, task)
        return Response({'detail': s[1]}, status=status.HTTP_200_OK if s[0] else status.HTTP_400_BAD_REQUEST)
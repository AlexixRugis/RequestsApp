from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from app.models.repair_requests.RepairTask import *
from app.services.RepairRequestsService import RepairRequestsService

class CompleteTaskView(views.APIView):
    permission_classes = (IsAuthenticated, )
    http_method = 'POST'

    def post(self, request, pk):
        account = get_object_or_404(RepairTask, pk=pk)
        s = RepairRequestsService.accept_request(request, account)
        return Response({'detail': s[1]}, status=status.HTTP_200_OK if s[0] else status.HTTP_400_BAD_REQUEST)
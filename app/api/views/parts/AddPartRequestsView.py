from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app.models.repair_requests.RepairTask import *
from app.services.RepairPartsService import *

class AddPartRequestsView(views.APIView):
    permission_classes = (IsAuthenticated, )
    http_method = 'POST'

    def post(self, request, pk):
        task = get_object_or_404(RepairTask, pk=pk)
        RepairPartsService.add_parts(task, request.data)
        return Response({'detail': 'ok'}, status=status.HTTP_200_OK)


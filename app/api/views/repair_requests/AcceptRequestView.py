from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from app.services.RepairRequestsService import *
from app.models.repair_requests.RepairRequest import *


class AcceptRequestView(views.APIView):
    permission_classes = (IsAuthenticated, )
    http_method = 'POST'

    def post(self, request, pk):
        account = get_object_or_404(RepairRequest, pk=pk)
        s = RepairRequestsService.accept_request(request, account)
        return Response({'detail': s[1]}, status=status.HTTP_200_OK if s[0] else status.HTTP_400_BAD_REQUEST)
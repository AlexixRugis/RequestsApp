from rest_framework import generics
from app.api.serializers.EmployeeSerializer import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from app.services.AccountService import AccountService

class MyAccountView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = EmployeeSerializer

    def get_object(self):
        return AccountService.get_account(self.request)
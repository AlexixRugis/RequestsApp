from rest_framework import views, status
from rest_framework.response import Response

from app.services.AccountService import AccountService

class LogoutView(views.APIView):
    permission_classes = ()
    http_method = 'POST'

    def post(self, request):
        s = AccountService.logout(request)
        return Response({'detail': s[1]}, status=status.HTTP_200_OK if s[0] else status.HTTP_400_BAD_REQUEST)
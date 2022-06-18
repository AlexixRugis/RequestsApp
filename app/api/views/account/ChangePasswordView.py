from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.services.AccountService import AccountService

class ChangePasswordView(views.APIView):
    permission_classes = (IsAuthenticated, )
    http_method = 'POST'

    def post(self, request):
        password = request.data.get('password', None)
        if not password:
            return Response({ "detail": "request should have password parameter" }, status=status.HTTP_400_BAD_REQUEST)

        s = AccountService.change_password(request, password)

        return Response({'detail': s[1]}, status=status.HTTP_200_OK if s[0] else status.HTTP_400_BAD_REQUEST)

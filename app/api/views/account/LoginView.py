from rest_framework import views, status
from rest_framework.response import Response

from app.services.AccountService import AccountService

class LoginView(views.APIView):
    permission_classes = ()
    http_method = 'POST'

    def post(self, request):
        phone_number = request.data.get('email', None)
        password = request.data.get('password', None)
        if not phone_number:
            return Response({ "detail": "request should have email parameter" }, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({ "detail": "request should have password parameter" }, status=status.HTTP_400_BAD_REQUEST)

        s = AccountService.login(request, phone_number, password)

        return Response({'detail': s[1]}, status=status.HTTP_200_OK if s[0] else status.HTTP_400_BAD_REQUEST)
from requests import Response

from app.services.AccountService import AccountService


from rest_framework import views, status
from rest_framework.response import Response
from app.services.AccountService import *

class IsAuthenticatedView(views.APIView):
    permission_classes = ()
    http_method = 'GET'

    def get(self, request):
        return Response({"is_authenticated": AccountService.is_authenticated(request)}, status = status.HTTP_200_OK)
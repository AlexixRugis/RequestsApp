from django.contrib.auth import authenticate, login as d_login, logout as d_logout
from django.utils.translation import gettext as _

class AccountService:
    @staticmethod
    def login(request, email, password):
        user = authenticate(username=email, password=password)

        if not user:
            return (False, _("Invalid email or password"))
        if not user.is_active:
            return (False, _("The user is inactive"))

        d_login(request, user)

        return (True, _("You have successfully logged in"))
    
    @staticmethod
    def logout(request):
        d_logout(request)
        return (True, _("You have successfully logged out"))

    @staticmethod
    def get_account(request):
        if request.user.is_authenticated:
            return request.user
        else:
            return None

    @staticmethod
    def is_authenticated(request):
        return request.user.is_authenticated
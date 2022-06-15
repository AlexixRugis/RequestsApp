from app.models.repair_requests.RepairRequest import *
from django.utils.translation import gettext as _

from app.models.repair_requests.RepairTask import RepairTask
from .AccountService import *

class RepairRequestsService:
    @staticmethod
    def get_available_requests():
        return RepairRequest.objects.filter(task=None).all()

    @staticmethod
    def accept_request(request, repair_request):
        executor = AccountService.get_account(request)

        if hasattr(repair_request, 'task'):
            return (False, _("This task is already accepted"))

        task = RepairTask(executor=executor, request=repair_request)
        task.save()

        return (True, _("Request is successfully accepted"))
        
    

from app.models.repair_requests.RepairTask import RepairTask
from .AccountService import *

class RepairTasksManager:
    @staticmethod
    def get_account_tasks(request):
        return RepairTask.objects.filter(executor=AccountService.get_account(request)).all()
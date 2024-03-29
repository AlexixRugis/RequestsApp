from django.utils.translation import gettext as _
from app.models.repair_requests.RepairTask import RepairTask
from .AccountService import *

class RepairTasksService:
    @staticmethod
    def get_account_tasks(request):
        return RepairTask.objects.filter(executor=AccountService.get_account(request), is_completed=False).all()

    @staticmethod
    def get_completed_tasks(request):
        return RepairTask.objects.filter(executor=AccountService.get_account(request), is_completed=True).all()

    @staticmethod
    def complete_task(request, task):
        executor = AccountService.get_account(request)

        file = request.data.get('image', None)

        if not file:
            return (False, _("You should attach a photo to complete a task"))
        
        if not task.executor == executor:
            return (False, _("You dont have permission to execute this action"))

        if task.is_completed:
            return (False, _("This task is already completed"))

        task.status_photo.save(file.name, file, save=True)
        task.is_completed = True
        task.save()

        return (True, _("Task is completed"))
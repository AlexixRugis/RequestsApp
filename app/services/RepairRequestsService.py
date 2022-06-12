from app.models.repair_requests.RepairRequest import *

class RepairRequestsService:
    @staticmethod
    def get_available_requests():
        return RepairRequest.objects.filter(task=None).all()
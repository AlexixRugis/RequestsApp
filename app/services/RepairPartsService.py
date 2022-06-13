from django.shortcuts import get_object_or_404

from app.models.parts.RepairPart import RepairPart
from app.models.parts.RepairPartRequest import *

class RepairPartsService:
    @staticmethod
    def add_parts(task, data):
        for part_request in data['parts']:
            pk = part_request['pk']
            amount = part_request['amount']

            part = get_object_or_404(RepairPart, pk=pk)

            request = RepairPartRequest(part=part, task=task, amount=amount)
            request.save()


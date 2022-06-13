from django.contrib import admin
from .models.parts.RepairPart import *
from .models.employees.Post import *
from .models.employees.Employee import *
from .models.repair_requests.RepairRequest import *

from .models.parts.RepairPartRequest import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Employee)

admin.site.register(RepairPart)
admin.site.register(RepairPartRequest)

admin.site.register(RepairTask)
admin.site.register(RepairRequest)


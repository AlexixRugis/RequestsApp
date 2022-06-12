from django.contrib import admin
from .models.parts.PartCategory import *
from .models.parts.RepairPart import *
from .models.employees.Post import *
from .models.employees.Employee import *
from .models.repair_requests.RepairRequest import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Employee)

admin.site.register(PartCategory)
admin.site.register(RepairPart)

admin.site.register(RepairRequest)

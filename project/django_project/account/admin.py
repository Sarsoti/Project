from django.contrib import admin
from .models import Employeeinfo,Companyinfo,User
# Register your models here.
admin.site.register(Employeeinfo)
admin.site.register(Companyinfo)
admin.site.register(User)
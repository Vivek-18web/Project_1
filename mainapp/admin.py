from django.contrib import admin
from .models import vacancy, berojgar, application, hrgroup

# Register your models here.

admin.site.register([vacancy,berojgar,application,hrgroup])
from django.contrib import admin
from staffs.models import Staff


class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'mobile', 'email', 'type']


admin.site.register(Staff, StaffAdmin)

from django.contrib import admin
from counts.models import Count


class CountAdmin(admin.ModelAdmin):
    list_display = ['student', 'current_student', 'teacher', 'client', 'courses']


admin.site.register(Count, CountAdmin)


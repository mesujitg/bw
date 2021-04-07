from django.contrib import admin
from courses.models import Course, Type


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'details', 'fee']


admin.site.register(Course, CourseAdmin)
admin.site.register(Type)

from django.contrib import admin

from students.models import Student, StudentCourse


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'email']


class MapAdmin(admin.ModelAdmin):
    list_display = ['student', 'course']


admin.site.register(Student, StudentAdmin)

admin.site.register(StudentCourse, MapAdmin)

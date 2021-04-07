from django.contrib import admin
from subscribers.models import Subscriber


class SubEmail(admin.ModelAdmin):
    list_display = ['email', 'date']


admin.site.register(Subscriber, SubEmail)

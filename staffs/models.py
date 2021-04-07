from django.db import models
from courses.models import Course


class Staff(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobile = models.IntegerField()
    email = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=[('Staff', 'Staff'), ('Teacher', 'Teacher')], default='Staff')
    course = models.ManyToManyField(Course, primary_key=False, null=True, blank=True)


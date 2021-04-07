from django.db import models


class Count(models.Model):
    student = models.IntegerField()
    current_student = models.IntegerField()
    teacher = models.IntegerField()
    client = models.IntegerField()
    courses = models.IntegerField()

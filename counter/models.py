from django.db import models


class Counter(models.Model):
    title = models.CharField(max_length=256)
    count = models.IntegerField()

    def __str__(self):
        return self.title

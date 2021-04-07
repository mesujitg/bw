from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=256)
    details = models.TextField()

    def __str__(self):
        return self.title

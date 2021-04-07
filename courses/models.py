from django.db import models


class Type(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.IntegerField()
    details = models.TextField()
    fee = models.FloatField()
    image = models.ImageField(upload_to='courses', null=True, blank=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ('name', 'duration', 'fee', 'details')



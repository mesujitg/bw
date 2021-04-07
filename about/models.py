from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class About(models.Model):
    title = models.CharField(max_length=256)
    details = RichTextUploadingField()
    image = models.ImageField(upload_to='about')

    def __str__(self):
        return self.title


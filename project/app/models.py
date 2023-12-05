from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


from django.db import models
from django.utils import timezone


# Create your models here.
class Job(models.Model):
    url = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        db_table = 'jobs'

    class Admin:
        pass

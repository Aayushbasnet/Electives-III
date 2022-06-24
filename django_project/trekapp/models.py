from django.db import models

# Create your models here.
class Trek(models.Model):
    title = models.CharField(max_length=200)
    days = models.CharField(max_length=200)
    start_destination = models.CharField(max_length=200)
    end_destination = models.CharField(max_length=200)
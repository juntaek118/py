# Create your models here.
from django.db import models

class Webtoon(models.Model):
    Name = models.CharField(max_length=30)
    List = models.CharField(max_length=50)
    New = models.CharField(max_length=50)
    Changed = models.BooleanField()
    Time = models.CharField(max_length=20)

    def __str__(self):
        return self.Name
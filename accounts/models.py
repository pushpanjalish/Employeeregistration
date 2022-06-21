from unicodedata import name
from django.db import models

# Create your models here.
class EmpModel(models.Model):
    name=models.CharField(max_length=250)
    age=models.CharField(max_length=250)

    def __str__(self):
        return self.name
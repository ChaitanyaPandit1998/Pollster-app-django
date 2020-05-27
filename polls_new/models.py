from django.db import models

# Create your models here.

class Bio(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  gender=models.CharField(max_length=15)
  age=models.IntegerField()


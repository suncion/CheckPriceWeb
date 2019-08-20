from django.db import models


# Create your models here.
class User(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    department = models.IntegerField()
    password = models.CharField(max_length=32)

class Department(models.Model):
    id=models.IntegerField()
    name=models.CharField(max_length=20)
    superior=models.IntegerField()
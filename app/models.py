from django.db import models

# Create your models here.

class Employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    eage=models.IntegerField()
    gender=models.CharField(max_length=20)

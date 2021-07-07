from django.db import models

class Data(models.Model):
    email=models.EmailField()
    pas=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=8)
    contact=models.CharField(max_length=10)
    contact2=models.CharField(max_length=10,blank=True)

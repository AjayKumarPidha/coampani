from django.db import models

# Create your models here.
class school(models.Model):
    gama=models.CharField(max_length=100,blank=True,null=True)
    nama=models.CharField(max_length=100,blank=True,null=True)
    fama=models.CharField(max_length=100,blank=True,null=True)
    dama=models.CharField(max_length=100,blank=True,null=True)
from django.db import models

# Create your models here.
class school(models.Model):
   
    sama=models.CharField(max_length=100,blank=True,null=True)
    jama=models.CharField(max_length=100,blank=True,null=True)
    lama=models.CharField(max_length=100,blank=True,null=True)
    dama=models.CharField(max_length=100,blank=True,null=True)
from __future__ import unicode_literals

from django.db import models

class Amazon(models.Model):
    x=models.DateField()
    y=models.DecimalField(max_digits=10,decimal_places=5,default=0.00)
    
class Facebook(models.Model):
    x=models.DateField()
    y=models.DecimalField(max_digits=10,decimal_places=5,default=0.00)
    
class Google(models.Model):
    x=models.DateField()
    y=models.DecimalField(max_digits=10,decimal_places=5,default=0.00)

class User_transact(models.Model):
    username=models.CharField(max_length=120,blank=True,null=True)
from __future__ import unicode_literals

from django.db import models

class Amazon(models.Model):
    x=models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    y=models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    describ=models.CharField(max_length=120,default='ecommerce')

class Facebook(models.Model):
    x=models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    y=models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    describ=models.CharField(max_length=120,default='ecommerce')

class Google(models.Model):
    x=models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    y=models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    describ=models.CharField(max_length=120,default='ecommerce')


class DynamicShare(models.Model):
    shareName=models.CharField(max_length=120,blank=True,null=True)
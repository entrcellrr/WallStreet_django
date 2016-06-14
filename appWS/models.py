from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.
class SignUp(models.Model):
    name=models.CharField(max_length=120,blank=False,null=True)
    email=models.EmailField()
    college=models.CharField(max_length=120,blank=False,null=True)
    branch=models.CharField(max_length=120,blank=False,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    password=models.CharField(max_length=120,blank=False,null=True)
    def __str__(self):
        return self.name

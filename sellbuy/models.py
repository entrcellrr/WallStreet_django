from __future__ import unicode_literals

from django.db import models

from django import forms
# Create your models here.

class Share(models.Model):
    name=models.CharField(max_length=120,blank=True,null=True)
    describ=models.CharField(max_length=120,blank=True,null=True)
    currentprice=models.DecimalField(max_digits=7,decimal_places=2,default=1000.0000)
    queries=models.IntegerField(default=0)
    queries_total=models.IntegerField(default=0)
	
    def __str__(self):
        return self.name
class News(models.Model):
    news=models.CharField(max_length=120,blank=True,null=True)
    weight=models.DecimalField(max_digits=4,decimal_places=2,default=-1)
    
    def __str__(self):
        return self.news
class Timer(models.Model):
    name=models.CharField(max_length=120,blank=True,null=True)
    time=models.IntegerField(default=0)	
    def __str__(self):
        return self.name


class ShareDetail(models.Model):
	id=models.IntegerField(primary_key='True')
	username=models.CharField(max_length=120,blank=True,null=True)
	money_in_hand=models.DecimalField(max_digits=20,decimal_places=2,default=10000.00)
	Xaviers_School=models.IntegerField(default=0)
	Wayne_Enterprises=models.IntegerField(default=0)
	Walter_White_Inc=models.IntegerField(default=0)
	Umbrella_Corp=models.IntegerField(default=0)
	STAR_Labs=models.IntegerField(default=0)
	Stark_Industries=models.IntegerField(default=0)
	Skynet=models.IntegerField(default=0)
	SHIELD=models.IntegerField(default=0)
	Pearson_Hardman=models.IntegerField(default=0)
	Palmer_Tech=models.IntegerField(default=0)
	Oscorp_RnD=models.IntegerField(default=0)
	Olivanders_Wand=models.IntegerField(default=0)
	Monsters_Inc=models.IntegerField(default=0)
	LexCorp=models.IntegerField(default=0)
	Illuminati_Consolidations=models.IntegerField(default=0)
	Hammer_Tech=models.IntegerField(default=0)
	Gringotts_Bank=models.IntegerField(default=0)
	Evil_Inc=models.IntegerField(default=0)
	Daily_Planet=models.IntegerField(default=0)
	Buzzinga_Entertainment=models.IntegerField(default=0)
	Bajrang_Cafe=models.IntegerField(default=0)
	Bakers_Street_Findings=models.IntegerField(default=0)
	Ammunation_Pharma=models.IntegerField(default=0)
	ACME=models.IntegerField(default=0)
	
	def __str__(self):
		return self.username

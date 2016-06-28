from __future__ import unicode_literals

from django.db import models

class Share_Data(models.Model):
    x=models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    y=models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    def __str__(self):
    	return self.x

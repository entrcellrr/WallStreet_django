from django.http import HttpResponse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *
from django.db import models
from django.apps import apps
from .models import DynamicShare
from django.contrib import admin
from django.conf import settings
from importlib import import_module
from django.core.urlresolvers import clear_url_caches

def graph(request,name):

	mymodel=apps.get_model('portfolio',name)

	query_x = mymodel.objects.values_list('x')
	query_y = mymodel.objects.values_list('y')
	plt.plot(query_x,query_y)

	response = HttpResponse(content_type='image/png')
	# create your image as usual, e.g. pylab.plot(...)

	plt.savefig(response, format="png")
	plt.close()
	return response
class mAdmin(admin.ModelAdmin):
	list_display=["x1"]	
i=11
def dynamic(request):
	attrs = {'x1': models.DecimalField(max_digits=7,decimal_places=2,default=0.00),
	'__module__': 'portfolio'}
	from django.core import management
	global i
	model = type("testx"+str(i), (models.Model,),attrs)

	admin.site.register(model,mAdmin)
	reload(import_module(settings.ROOT_URLCONF))
	clear_url_caches()
	
	management.call_command('makemigrations', interactive=False)
	management.call_command('migrate', interactive=False)
	
	i+=1

	return HttpResponse("hello")

"""
shell command instruction
import csv
with open(path) as f:
	reader = csv.reader(f,delimiter=',')
	i = 1
	for row in reader:
		name.objects.create(x=i,y=row[1])
		i+=1
"""

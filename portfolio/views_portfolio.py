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

"""
shell command instruction
import csv
with open(path) as f:
	reader = csv.reader(f,delimiter=',')
	for row in reader:
		newnumber = ''
		for o in row[1]:
			if o != ',':
				newnumber+=o
		name.objects.create(x=row[0][0:10],y=float(newnumber))
"""

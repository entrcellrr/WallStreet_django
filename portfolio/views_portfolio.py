from django.http import HttpResponse
from .models import DynamicShare
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *
from django.db import models
from django.apps import apps

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
from django.http import HttpResponse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *
from sellbuy .models import *
from django.db import models
from django.apps import apps
from django.contrib import admin
from django.conf import settings
from importlib import import_module
from .models import *
from .admin import *
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

i = 0
Matrix = [['0' for x in range(1000)] for y in range(100)]
Matrixc = 0
Matrixr = 0
for o in ShareDetail.objects.all():
	Matrix[Matrixr][0]=o.username
	Matrix[Matrixr][1]=i
	Matrixr+=1 


from django.http import HttpResponse
from .models import Share_Data, DynamicShare
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *
from django.db import models
from django.db.models.signals import class_prepared
def barchart(request):
	query_x = Share_Data.objects.values_list('x')
	query_y = Share_Data.objects.values_list('y')
	plt.plot(query_x,query_y)

	response = HttpResponse(content_type='image/png')
	# create your image as usual, e.g. pylab.plot(...)

	plt.savefig(response, format="png")
	return response
i=0
def testDynamic(request):
	global i
	i+=1
	x1 = models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
	x='x'+str(i)
	x1.contribute_to_class(DynamicShare,x)
	return HttpResponse()
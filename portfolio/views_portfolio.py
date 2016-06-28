from django.http import HttpResponse
from .models import *
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *
from django.db import models
from django.db.models.signals import class_prepared
def graph1(request):
	plt.close()
	query_x = Amazon.objects.values_list('x')
	query_y = Amazon.objects.values_list('y')
	plt.plot(query_x,query_y)
	response = HttpResponse(content_type='image/png')
	plt.savefig(response, format="png")
	return response

def graph2(request):
	plt.close()
	query_x = Google.objects.values_list('x')
	query_y = Google.objects.values_list('y')
	plt.plot(query_x,query_y)
	response = HttpResponse(content_type='image/png')
	plt.savefig(response, format="png")
	return response

def graph3(request):
	plt.close()
	query_x = Facebook.objects.values_list('x')
	query_y = Facebook.objects.values_list('y')
	plt.plot(query_x,query_y)
	response = HttpResponse(content_type='image/png')
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
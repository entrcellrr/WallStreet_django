from django.http import HttpResponse
from .models import Share_Data
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *

def barchart(request):
	query_x = Share_Data.objects.values_list('x')
	query_y = Share_Data.objects.values_list('y')
	plt.plot(query_x,query_y)

	response = HttpResponse(content_type='image/png')
	# create your image as usual, e.g. pylab.plot(...)

	plt.savefig(response, format="png")
	return response


	


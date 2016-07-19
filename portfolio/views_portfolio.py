from django.http import HttpResponse
import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
#from matplotlib import pylab
#from pylab import *
from sellbuy .models import *
from django.db import models
from django.apps import apps
from django.contrib import admin
from django.conf import settings
from importlib import import_module
from .models import *
from .admin import *
from django.core.urlresolvers import clear_url_caches
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from sellbuy.models import Share, ShareDetail,Timer,News
import csv
from plotly.offline import plot
from plotly.graph_objs import Bar, Scatter, Figure, Layout
import numpy as np
def graph(request,name):
	
	
	mymodel=apps.get_model('portfolio',name)

	#'query_x = mymodel.objects.values_list('x')
	#'query_y = mymodel.objects.values_list('y')
	x1=[]
	y1=[]
	for o in mymodel.objects.all():
			
		x1.append(o.x)
		y1.append(int(o.y))


	#plt.plot(query_x,query_y)
	

	return HttpResponse(plot([Bar(x=x1, y=y1)],auto_open=False,output_type='div'))

@login_required
def portfolio(request):
	#dataimg='<img style="-webkit-user-select: none; cursor: zoom-in;" src="./graph/'+request.user+'"width="147" height="110">'
	#dict={data:da}
	
#def fetch_portfolio_graph(request):
	file_data = np.loadtxt('portfolio.csv', delimiter=' ',dtype='str')
	Matrix=file_data
	f = open ( 'portfolio_dim_r.txt')
	for row in f:
		Matrixr =int(row)
	f = open ( 'portfolio_dim_c.txt')
	for col in f:
		Matrixc=int(col)


	y_array = [float(0) for x in range(0,Matrixc-1)]
	for x in range(0,Matrixr):
		if(str(Matrix[x][0])==str(request.user)):
			for col in range(1,Matrixc):
				y_array[col-1]=int(float(Matrix[x][col]))
	
	x_array = [x for x in range(0,Matrixc-1)]
	print x_array
	print y_array
	#plt.plot(x_array,y_array)
	'''response = HttpResponse(content_type='image/png')
	plt.savefig(response, format="png")
	plt.close()
	'''
	graph_str=plot([Scatter(x=x_array, y=y_array)],auto_open=False,output_type='div')
	return render_to_response('portfolio/portfolio.html',{'name':request.user,'graph':graph_str})

def leader_board(request):
	
	return response

def download(request):
	file_data = np.loadtxt('portfolio.csv', delimiter=' ',dtype='str')
	Matrix=file_data
	f = open ( 'portfolio_dim_r.txt')
	for row in f:
		Matrixr =int(row)
	f = open ( 'portfolio_dim_c.txt')
	for col in f:
		Matrixc=int(col)#global t
	#response = HttpResponse(content_type='text/csv')
	#from .utils import queryset_to_workbook
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename="somefilename.xls"'
	#t+=1
	#response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-16'
    
	writer = csv.writer(response,delimiter='\t')
	#writer.writerow(['sep=,'])
	writer.writerows(Matrix)
	return response
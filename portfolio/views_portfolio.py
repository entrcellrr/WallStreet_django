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
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from sellbuy.models import Share, ShareDetail,Timer,News
import csv
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
'''
file_data = np.loadtxt('portfolio.csv', delimiter=' ',dtype='str')
Matrix=file_data


f = open ( 'portfolio_dim_r.txt')
for row in f:
	Matrixr =int(row)
f = open ( 'portfolio_dim_c.txt')
for col in f:
	Matrixc=int(col)
'''
@login_required
def portfolio(request):
	#dataimg='<img style="-webkit-user-select: none; cursor: zoom-in;" src="./graph/'+request.user+'"width="147" height="110">'
	#dict={data:da}
	return render_to_response(
		'portfolio/portfolio.html',{'name':request.user})

def fetch_portfolio_graph(request):
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
				y_array[col-1]=Matrix[x][col]
	
	x_array = [x for x in range(0,Matrixc-1)]
	print x_array
	print y_array
	plt.plot(x_array,y_array)
	response = HttpResponse(content_type='image/png')
	plt.savefig(response, format="png")
	plt.close()
	return response
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
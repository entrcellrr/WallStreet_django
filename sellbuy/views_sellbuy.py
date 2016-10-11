from django.shortcuts import render
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sellbuy.models import Share, ShareDetail,Timer,News
from login.models import UserDetail
from .forms import ListForm
from django.core import serializers
from django.http import JsonResponse
import json,threading#,datetime
import random
import numpy as np
import multiprocessing as mp
#from portfolio import views_portfolio as vp# import Matrix,Matrixr,Matrixc
from sellbuy.WallStreet import SharePriceOutputWithoutNews as SPW
from django.apps import apps
i=-2
userstr=''


@login_required
def current_priceAjax(request):

	data=Share.objects.all().exclude(describ='All')
	global userstr
	userstr=str(request.user)
	popup='<script language="javascript" type="text/javascript">function popitup(url) {var leftPosition, topPosition;leftPosition = (window.screen.width / 2) - ((800 / 2) + 10);topPosition = (window.screen.height / 2) - ((600 / 2) + 50);newwindow=window.open(url,\'name\',"status=no,height=600,width=800,resizable=yes,left="+ leftPosition + ",top=" + topPosition + ",screenX=" + leftPosition + ",screenY="+ topPosition + ",toolbar=no,menubar=no,scrollbars=no,directories=no");if (window.focus) {newwindow.focus()}return false;}</script>'	
	
	strdata='<table>'
	global i
	print "i=================",i
	if i ==-2:
		print "timer_started"
		i=30
		p1=mp.Process(name='fun_call',target=fun_call)
		p1.start()
		from django.db import connection
		connection.close()

	for o in data:
		qty = ShareDetail.objects.values_list(str(o.name)).filter(username=request.user)
		var_qty = qty[0][0]
		strdata+='<tr><td><a href='+'\'./share_graph/'+str(o.name)+'\' onclick=\"return popitup(\'./share_graph/'+str(o.name)+'\')\">'+str(o.name)+'</a>'+'</td><td>'+str(o.currentprice)+'</td><td width=25 align=\'center\'>'+str(var_qty)+'</td></tr>'
	strdata+='</table>'	
	
	#strdata+='</table></marquee>'	
	return HttpResponse(strdata)

@login_required
def current_news(request):

	data=News.objects.all()
	
	
	userstr=str(request.user)
	strnews='<marquee onmouseover="this.stop()" onmouseout="this.start()" direction="up" height =40 scrolldelay=300><table>'
	#xyz=0
	for o in data:
		#share = Share.objects.get(id = xyz)
		#x = share.name
		#xyz=xyz+1
		strnews+='<tr><td>'+ ''+ str(o.news)+'</td></tr>'
	strnews+='</table></marquee>'	
	
	#strdata+='</table></marquee>'	
	return HttpResponse(strnews)

def current_queries(request):

	data=Share.objects.all()
	str_queries='<table>'
	for o in data:
		str_queries+='<tr><td>'+str(o.name)+'</td><td>'+str(o.queries)+'</td><td>'+str(o.queries_total)+'</td></tr>'
	str_queries+='</table>'
	return HttpResponse(str_queries)


def timer_update(request):
	
	time_data=Timer.objects.all().filter(name='timerUpdate')
	time =[(o.time)for o in time_data]
	#print "time shown"+str(time)
	return HttpResponse(time)

countMinute = 0.0
#import pickle
def UpdatePortfolio():
	file_data = np.loadtxt('portfolio.csv', delimiter=' ',dtype='str')
	Matrix=file_data
	f = open ( 'portfolio_dim_r.txt')
	for row in f:
		Matrixr =int(row)
	f = open ( 'portfolio_dim_c.txt')
	for col in f:
		Matrixc=int(col)
	print "updated"
	user = ShareDetail.objects.all()
	shares = Share.objects.exclude(name='none').all()
	print "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMatrixc="+str(Matrixc)
	
	for o in user:
		shareworth = float(0)
		for sh in shares:
			shareworth += float(getattr(o,str(sh.name))) * float(sh.currentprice)
		UserNetWorth = float(o.money_in_hand) + shareworth
		for x in range(0,Matrixr):
			print "matrixr loop started"
			print Matrix[x][0],o.username
			if(str(Matrix[x][0])==o.username):
				Matrix[x][Matrixc]=UserNetWorth
	Matrixc+=1
	if Matrixc>=950:
		Matrixc=2
	np.savetxt("portfolio.csv",Matrix,fmt='%s')
	with open('portfolio_dim_r.txt', 'w') as f:
		f.write(str(Matrixr))
	with open('portfolio_dim_c.txt', 'w') as f:
		f.write(str(Matrixc))

#from apscheduler.schedulers.background import BackgroundScheduler
def printit(iter_count):
	iter_count=int(iter_count/15)
	#global userstr
	#print "process="+str(multiprocessing.current_process().name)
	global countMinute
	modelt = Timer.objects.get(name='timerUpdate')
	timer=modelt.time
	timer-=1
	if timer<=-1:
		timer=15
		countMinute+=0.5
		if countMinute == 0.5:
			#################################  to update portfolio
			UpdatePortfolio()
			countMinute = 0
	print timer
	setattr(modelt,'time',timer)
	modelt.save()
	if timer==5:
		#n = random.random()
		###############################################the algo to be executed every 30 secs
		share_querylist=Share.objects.all().exclude(name='None')
		share_index=0
		for o in share_querylist:
			#(1,10) # returns a random integer

			cp=o.currentprice
			if(int(cp<2)):
				cp=5
			#print "sh index",share_index," sh name",o.name
			#print iter_count
			n = SPW(share_index,float(cp)*float(1.1),iter_count)
			#n=n*1.09
			
			c=1.01#afterwards will be synce with news also
			queries_total=float(o.queries_total)
			if(queries_total)<1:
				queries_total=1;
			new_price=float(n*(1+(1/5)*float((o.queries/queries_total))))
			if(new_price<2):
				new_price=5
			print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",cp ,n,new_price
			setattr(o,'currentprice',new_price)
			setattr(o,'queries',0)
			setattr(o,'queries_total',0)	
			o.save()
			currentshare=apps.get_model('portfolio',o.name)
			currentshare.objects.create(x=iter_count,y=new_price)					
			share_index+=1
		#	print o.name
		#share_querylist.save()
		#######################################################################################
	#threading.Timer(1.0, printit).start()
#apsched = BackgroundScheduler()
#apsched.start()
#apsched.add_job(printit, 'interval', seconds=1)
import time
	
def fun_call():
	from django.db import connection
	connection.close()
	while(1):
		modeliter = Timer.objects.get(name='iter')
		iter_count=modeliter.time
		printit(iter_count)
		setattr(modeliter,'time',iter_count+1)
		modeliter.save()
		time.sleep(1)


def dynamic2(request):
	file_data = np.loadtxt('portfolio.csv', delimiter=' ',dtype='str')
	Matrix=file_data
	f = open ( 'portfolio_dim_r.txt')
	for row in f:
		Matrixr =int(row)
	f = open ( 'portfolio_dim_c.txt')
	for col in f:
		Matrixc=int(col)
	
	#global Matrix,Matrixr,Matrixc
	data='<table>'
	for row in range (0,Matrixr):
		data+='<tr>'
		for col in range (0,Matrixc):
			data+='<td>'+ str(Matrix[row][col])+'</td>'
		data+='</tr>'
	data+='</table>'
	return HttpResponse(data)

@login_required
def sellbuyhome(request):
	Desc='All'
	name_return = 'ACME'
	error=''
	print"??????????????????????????????????????????????????????????????"+str(request.user)
	if request.method == 'POST':
		Desc = request.POST.get("ShareDescrib")
		name_return = request.POST.get("ShareName")
		try:
			qty1= int(request.POST.get('Qty'))
		except:
			qty1=int(0)
		user_query=ShareDetail.objects.get(username=request.user)
		money=user_query.money_in_hand
			
		share_query=Share.objects.get(name=name_return)
		share_price=share_query.currentprice
		qty_share_query=share_query.queries
		if qty1>=int(0):
			if request.POST.get("buy")=='BUY':
			
			
				if(qty1*share_price>money):
					error='Money is less.Only '+str(int(money/share_price))+' shares can be bought'
				else:
					var_qty2 = ShareDetail.objects.values_list(name_return).filter(username=request.user)
					qty2 = var_qty2[0][0]
					setattr(user_query,name_return,qty1+qty2)
				
					setattr(user_query,'money_in_hand',money-(share_price*qty1))
					user_query.save()
					queries_total=share_query.queries_total
					queries_total=queries_total+qty1
					setattr(share_query,'queries_total',queries_total)
					setattr(share_query,'queries',qty1+qty_share_query)
					share_query.save()
					#print "user money"+str(user_query.money_in_hand)
					error='success'

			if request.POST.get("sell")=='SELL':

				var_qty2 = ShareDetail.objects.values_list(name_return).filter(username=request.user)
				qty2 = var_qty2[0][0]
				if qty1<=qty2:
					setattr(user_query,name_return,qty2-qty1)
					setattr(user_query,'money_in_hand',money+share_price*qty1)
					user_query.save()
					queries_total=share_query.queries_total
					queries_total=queries_total+qty1
					setattr(share_query,'queries',qty_share_query-qty1)
					setattr(share_query,'queries_total',queries_total)
					share_query.save()
					error='success'
				else:
					error='you dont have that many shares'
		else:
			error='we take our event rather seriously'
	print request.user
	user_query=ShareDetail.objects.get(username=request.user)
	print "line crossed"
	form = ListForm(None, SDesc=Desc, Sname = name_return,UserName=request.user)
	variables = RequestContext(request,{
		'form':form,
		'name':request.user,
		'error':error,
		'money':user_query.money_in_hand,
		})
	return render_to_response(
   	    'sellbuy/transact.html',variables,
     	)
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

i=-2
userstr=''

@login_required
def current_priceAjax(request):

	data=Share.objects.all().exclude(describ='All')
	global userstr
	userstr=str(request.user)
	strdata='<marquee onmouseover="this.stop()" onmouseout="this.start()" direction="up" height =40 scrolldelay=300><table>'
	strdata='<table>'
	
	global i
	if i is -2:
		i=30
		printit()
	for o in data:

		strdata+='<tr><td>'+str(o.name)+'</td><td>'+str(o.currentprice)+'</td></tr>'
	strdata+='</table>'	
	
	#strdata+='</table></marquee>'	
	return HttpResponse(strdata)

@login_required
def current_news(request):

	data=News.objects.all()
	userstr=str(request.user)
	strnews='<marquee onmouseover="this.stop()" onmouseout="this.start()" direction="up" height =40 scrolldelay=300><table>'
	for o in data:
		strnews+='<tr><td>'+str(o.news)+'</td></tr>'
	strnews+='</table>'	
	
	#strdata+='</table></marquee>'	
	return HttpResponse(strnews)


def timer_update(request):
	time_data=Timer.objects.all().filter(name='timerUpdate')
	return HttpResponse([(o.time)for o in time_data])

def printit():
	global i
	global userstr
	threading.Timer(1.0, printit).start()
	i=i-1
	model = Timer.objects.get(name='timerUpdate')
	if i==-1:
		i=30
	print i
	setattr(model,'time',i)
	model.save()
	#print "Hello, World!",i,userstr
  

@login_required
def sellbuyhome(request):

	if request.method == 'POST':
		Desc = request.POST.get("ShareDescrib")
		name_return = request.POST.get("ShareName")
###################################################################################################3
		if request.POST.get("buy")=='BUY':
			qty1=int(request.POST.get("Qty"))
			money=ShareDetail.objects.get(name=request.user)		
			print 'buy pressed'
#####################################################################################################
		if request.POST.get("sell")=='SELL':
			qty1=request.POST.get("Qty")
			
			print 'sell pressed'
##################################################################################################			
	else:
		Desc='All'
		name_return = 'share1'
		
	form = ListForm(None, SDesc=Desc, Sname = name_return,UserName=request.user)
	variables = RequestContext(request,{
		'form':form,
		'name':request.user,
	#	'latupdated_time':datetime.datetime.now()
		})
	return render_to_response(
   	    'sellbuy/transact.html',variables,
     	)
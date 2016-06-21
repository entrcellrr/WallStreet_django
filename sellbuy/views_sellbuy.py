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
	Desc='All'
	name_return = 'share1'
	error=''
	
	if request.method == 'POST':
		Desc = request.POST.get("ShareDescrib")
		name_return = request.POST.get("ShareName")
		qty1=int(request.POST.get("Qty"))
		user_query=ShareDetail.objects.get(username=request.user)
		money=user_query.money_in_hand
			
		share_query=Share.objects.get(name=name_return)
		share_price=share_query.currentprice
		
		if request.POST.get("buy")=='BUY':
			
			
			if(qty1*share_price>money):
				error='Money is less.Only '+str(int(money/share_price))+' shares can be bought'
			else:
				var_qty2 = ShareDetail.objects.values_list(name_return).filter(username=request.user)
				qty2 = var_qty2[0][0]
				setattr(user_query,name_return,qty1+qty2)
				setattr(user_query,'money_in_hand',money-share_price*qty1)
				user_query.save()
				#print "user money"+str(user_query.money_in_hand)
				error='success'

		if request.POST.get("sell")=='SELL':

			var_qty2 = ShareDetail.objects.values_list(name_return).filter(username=request.user)
			qty2 = var_qty2[0][0]
			setattr(user_query,name_return,qty2-qty1)
			setattr(user_query,'money_in_hand',money+share_price*qty1)
			user_query.save()
			#print "user money"+str(user_query.money_in_hand)
			error='success'
		
	user_query=ShareDetail.objects.get(username=request.user)
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
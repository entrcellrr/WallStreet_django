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
from portfolio.views_portfolio import Matrix
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
	if i is -2:
		i=30
		printit()
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
	for o in data:
		strnews+='<tr><td>'+str(o.news)+'</td></tr>'
	strnews+='</table></marquee>'	
	
	#strdata+='</table></marquee>'	
	return HttpResponse(strnews)

def current_queries(request):

	data=Share.objects.all()
	str_queries='<table>'
	for o in data:
		str_queries+='<tr><td>'+str(o.name)+'</td><td>'+str(o.queries)+'</td></tr>'
	str_queries+='</table>'
	return HttpResponse(str_queries)


def timer_update(request):
	
	time_data=Timer.objects.all().filter(name='timerUpdate')
	time =[(o.time)for o in time_data]
	print "time shown"+str(time)
	return HttpResponse(time)


def printit():
	#global userstr
	modelt = Timer.objects.get(name='timerUpdate')
	i=modelt.time
	i=i-1
	if i<=-1:
		i=30
	print i
	setattr(modelt,'time',i)
	modelt.save()
	if i==5:
		#n = random.random()
		###############################################the algo to be executed every 30 secs
		share_querylist=Share.objects.all()
		for o in share_querylist:
			#(1,10) # returns a random integer
			cp=o.currentprice
			n = random.random()
			#the value of n is currently randomized
			#afterwards will be synce with news also
			setattr(o,'currentprice',int(float(cp)*float(1+o.queries*float(n/800))))
			setattr(o,'queries',0)	
			o.save()
		#	print o.name
		#share_querylist.save()
		#######################################################################################
	threading.Timer(1.0, printit).start()
	
def dynamic2(request):
	i = 0
	global storedata
	uname='<table>'
	t=0
	for o in ShareDetail.objects.all():
		uname+='<tr>'
		uname+='<td>'+Matrix[t][0]+'</td>'
		uname+='<td>'+str(Matrix[t][1])+'</td>'
		uname+='</tr>'
		t+=1
	uname+='</table>'
 	return HttpResponse(Matrix)

@login_required
def sellbuyhome(request):
	Desc='All'
	name_return = 'share1'
	error=''
	print"??????????????????????????????????????????????????????????????"+str(request.user)
	if request.method == 'POST':
		Desc = request.POST.get("ShareDescrib")
		name_return = request.POST.get("ShareName")
		qty1=int(request.POST.get("Qty"))
		user_query=ShareDetail.objects.get(username=request.user)
		money=user_query.money_in_hand
			
		share_query=Share.objects.get(name=name_return)
		share_price=share_query.currentprice
		qty_share_query=share_query.queries
		if request.POST.get("buy")=='BUY':
			
			
			if(qty1*share_price>money):
				error='Money is less.Only '+str(int(money/share_price))+' shares can be bought'
			else:
				var_qty2 = ShareDetail.objects.values_list(name_return).filter(username=request.user)
				qty2 = var_qty2[0][0]
				setattr(user_query,name_return,qty1+qty2)
				
				setattr(user_query,'money_in_hand',money-(share_price*qty1))
				user_query.save()
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
				setattr(share_query,'queries',qty_share_query-qty1)
				share_query.save()
				error='success'
			else:
				error='you dont have that many shares'
		
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
from django.shortcuts import render
from login.forms import *
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sellbuy.models import Share, ShareDetail,Timer
from login.models import UserDetail
from .forms import ListForm
from django.core import serializers
from django.http import JsonResponse
import json
# Create your views here.
import threading
i=0
userstr=''
@login_required
def current_priceAjax(request):

	data=Share.objects.all().exclude(describ='All')
	global userstr
	userstr=str(request.user)
	strdata='<marquee onmouseover="this.stop()" onmouseout="this.start()" direction="up" height =40 scrolldelay=300><table>'
	global i
	if i is 0:
		printit()
		i=1
	for o in data:

		strdata+='<tr><td>'+str(o.name)+'</td><td>'+str(o.currentprice)+'</td></tr>'
	strdata+='</table></marquee>'	
	return HttpResponse(strdata)

def timer_update(request):

	time_data=Timer.objects.all().filter(name='timerUpdate')
	return HttpResponse([(o.time)for o in time_data])


def printit():
	global i
	global userstr
	threading.Timer(1.0, printit).start()
	i=i+1
	print "Hello, World!",i,userstr
  

@login_required
def sellbuyhome(request):

	if request.method == 'POST':
		Desc = request.POST.get("ShareDescrib")
		name_return = request.POST.get("ShareName")
	else:
		Desc='All'
	
		name_return = 'share1'
	form = ListForm(None, SDesc=Desc, Sname = name_return,UserName=request.user)
	variables = RequestContext(request,{
		'form':form,
		'name':request.user
		})
	return render_to_response(
   	    'sellbuy/transact.html',variables,
     	)



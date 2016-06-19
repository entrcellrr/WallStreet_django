from django.shortcuts import render
from login.forms import *
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sellbuy.models import Share, ShareDetail
from login.models import UserDetail
from .forms import ListForm
from django.core import serializers
from django.http import JsonResponse
import json
# Create your views here.

@login_required
def current_priceAjax(request):

	#updated =serializers.serialize('xml',Share.objects.all().exclude(describ='All'))
	
	#data=serializers.serialize('xml',Share.objects.all().exclude(describ='All'),fields=('name','currentprice'))
	data=Share.objects.all().exclude(describ='All')
	
	strdata='<table>'
	for o in data:
		print o.currentprice
		strdata+='<tr><td>'+str(o.name)+'</td><td>'+str(o.currentprice)+'</td></tr>'
	strdata+='</table>'	
	#serializers.serialize('xml',Share.objects.all().exclude(describ='All'),fields=('name','currentprice'), stream=out)
	#data = serializers.serialize('xml', SomeModel.objects.all(), fields=('name','size'))
	return HttpResponse(strdata)
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



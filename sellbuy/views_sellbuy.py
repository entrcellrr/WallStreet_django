from django.shortcuts import render
from login.forms import *
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sellbuy.models import Share, ShareDetail
from login.models import UserDetail
# Create your views here.
@login_required
def sellbuyhome(request):
	user = UserDetail.objects.get(name=request.user)
	shares = Share.objects.all()
	id = user.name
	attr_filter=request.GET.get("ShareDescrib")
	attr = request.GET.get("branch")
	if attr is not None:
		model = ShareDetail.objects.get(username=id)
		qty2 = int(request.GET.get("QTY"))
		qty1 = getattr(model, attr)
		if request.GET.get("sell") == 'SELL':
			if qty2 > qty1:
				qty2 = qty1
			qty2 = -qty2
		setattr(model, attr, qty1+qty2)
		model.save()
	queryset=Share.objects.all()
	flshare=Share.objects.filter(describ=attr_filter)
	flshare1=queryset 
	context_data={
		"name":user.name,
		"describ_list":queryset,
		"share_filtered":flshare
	}
	context_default={
		"name":user.name,
		"describ_list":queryset,
		"share_filtered":flshare1
	}
	if attr_filter is not None:
		return render_to_response(
   	    	'sellbuy/transact.html',context_data
     		)
	else:
		return render_to_response(
			'sellbuy/transact.html',context_default
			)

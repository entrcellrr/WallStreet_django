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
	id = user.name
	attr = request.GET.get("branch")
	attr_filter=request.GET.get("ShareDescrib")
	model = ShareDetail.objects.get(username=id)
	if attr is not None:
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
	context_data={
		"name":user.name,
		"describ_list":queryset,
		"share_filtered":flshare
	}
	return render_to_response(
   	    'sellbuy/transact.html',context_data
     	)

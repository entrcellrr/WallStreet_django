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
	if request.method == 'GET':
		id = user.name
		name = request.GET.get("branch")
		qty = request.GET.get("QTY")
		s = ShareDetail.objects.get(username = id)
	    
	queryset=Share.objects.all()
	context_data={
		"name":user.name,
		"object_list":queryset,
	}
	return render_to_response(
   	    'sellbuy/transact.html',context_data
     	)


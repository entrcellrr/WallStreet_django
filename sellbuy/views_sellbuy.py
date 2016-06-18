from django.shortcuts import render
from login.forms import *
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sellbuy.models import Share, ShareDetail
from login.models import UserDetail
from .forms import ListForm#,Form_Calculated
# Create your views here.
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



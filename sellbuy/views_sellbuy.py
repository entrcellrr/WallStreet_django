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
# Create your views here.
@login_required
def sellbuyhome(request):
	
	if request.method == 'POST':
		Desc = request.POST.get("ShareDescrib")
		#Desc=form.cleaned_data['ShareDescrib']
	else:

		Desc='abd'
	form = ListForm(request.POST or None, SDesc=Desc)
	

	variables = RequestContext(request,{'form':form})
	return render_to_response(
   	    'sellbuy/transact.html',variables,
     	)



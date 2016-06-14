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
@csrf_protect
@login_required
def sellbuyhome(request):
	queryset=Share.objects.all()
	share=Share.objects.all()
	user = UserDetail.objects.get(name=request.user)
	context_data={
		"name":user.name,
		"object_list":queryset,
		"shares":share
	}
	return render_to_response(
    	'sellbuy/transact.html',context_data
        )

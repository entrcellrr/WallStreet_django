from django.shortcuts import render
from login.forms import *
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sellbuy.models import ShareDetail
from login.models import UserDetail
# Create your views here.@login_required
@csrf_protect
@login_required
def sellbuyhome(request):
    user = UserDetail.objects.get(name=request.user)
    id = user.id
    dict = {'id':id}

    return render_to_response(
        'sellbuy/transact.html',
        {'dict': dict}
        )

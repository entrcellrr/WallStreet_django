from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sellbuy.models import ShareDetail
from .models import UserDetail
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        no = ShareDetail.objects.count()
        if no == None:
            number= 1
        else:
            number= no + 1
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            sharedetail=ShareDetail.objects.create(
            username=form.cleaned_data['username'],
            id=number
                )
            userdetail=UserDetail.objects.create(
            name=form.cleaned_data['username'],
            id=number,
            email=form.cleaned_data['email'],
            branch=form.cleaned_data['branch'],
            college=form.cleaned_data['college'],
            contact=form.cleaned_data['contact'],
                )
    
            return HttpResponseRedirect('/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def registersuccess(request):
    return render_to_response(
        'registration/success.html',
        )

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):
    user = UserDetail.objects.get(name=request.user)
    name = user.name

    return render_to_response(
        'login/home.html',
        {'name': name}
        )

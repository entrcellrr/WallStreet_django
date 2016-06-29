from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sellbuy.models import ShareDetail
from .models import UserDetail
from importlib import import_module
from django.core.urlresolvers import clear_url_caches
from django.db import models
from django.apps import apps
from django.contrib import admin
from django.conf import settings
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
    
            #######################################################################################################3
            attrs = {'x': models.DecimalField(max_digits=7,decimal_places=2,default=0.00),
            'y': models.DecimalField(max_digits=7,decimal_places=2,default=0.00),
            '__module__': 'portfolio'}
            from django.core import management

            model = type('user_'+str(form.cleaned_data['username']), (models.Model,),attrs)
            class mAdmin(admin.ModelAdmin):
                list_display=["x","y"]
            admin.site.register(model,mAdmin)
            reload(import_module(settings.ROOT_URLCONF))
            clear_url_caches()
    
            management.call_command('makemigrations', interactive=False)
            management.call_command('migrate', interactive=False)
    

    ##################################################################################################
 

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

flag=0

@login_required
def home(request):
    user = UserDetail.objects.get(name=request.user)
    name = user.name
    from django.core import management
    if flag==0:
        reload(import_module(settings.ROOT_URLCONF))
        clear_url_caches()
    
        management.call_command('makemigrations', interactive=False)
        management.call_command('migrate', interactive=False)
        flag=1

    return render_to_response(
        'login/home.html',
        {'name': name}
        )
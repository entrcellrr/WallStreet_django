# -*- coding: utf-8 -*-
from django import forms
from .models import Share
from sellbuy.models import Share, ShareDetail
from login.models import UserDetail
class ShareForm(forms.ModelForm):
    class Meta:
        model=Share
        fields=['name','describ','currentprice']
queryset=Share.objects.values_list('describ','describ').order_by('describ').distinct()
    
class ListForm(forms.Form):
    #queryset=Share.objects.all()

    relevance = forms.ChoiceField(#initial=prev,
    	widget=forms.Select(),required=True,choices=[(o) for o in queryset])
       
def clean_name(self):
    name= self.cleaned_data.get('name')
    return name
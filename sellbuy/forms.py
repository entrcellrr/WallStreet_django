# -*- coding: utf-8 -*-
from django import forms
from .models import Share
from sellbuy.models import Share, ShareDetail
from login.models import UserDetail

class ShareForm(forms.ModelForm):
    class Meta:
        model=Share
        fields=['name','describ','currentprice']

class ListForm(forms.Form):
    def __init__(self,*args,**kwargs):

        super(ListForm,self).__init__(*args,**kwargs)

        
        queryset=Share.objects.values_list('describ','describ').order_by('describ').distinct()
        self.fields['ShareDescrib'] = forms.ChoiceField(widget=forms.Select(attrs={'onChange':'this.form.submit()'}),
        required=True,
        choices=[(o) for o in queryset])

        self.initial['ShareDescrib'] = self.fields['ShareDescrib'].choices[1][1]
###################################################
#    ShareDescrib,initial={'ab': 'ab'}

def clean_name(self):
    name= self.cleaned_data.get('name')
    return name
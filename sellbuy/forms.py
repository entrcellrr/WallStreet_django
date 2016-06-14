# -*- coding: utf-8 -*-
from django import forms
from .models import Share

class ShareForm(forms.ModelForm):
    class Meta:
        model=Share
        fields=['name','describ','currentprice']



def clean_name(self):
    name= self.cleaned_data.get('name')
    return name
# -*- coding: utf-8 -*-
from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=SignUp

        fields=['name','email','college','branch','password']




def clean_name(self):
    name= self.cleaned_data.get('name')
    return name
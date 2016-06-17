# -*- coding: utf-8 -*-
from django import forms
from sellbuy.models import Share, ShareDetail
from login.models import UserDetail

class ShareForm(forms.ModelForm):
    class Meta:
        model=Share
        fields=['name','describ','currentprice']

class ListForm(forms.Form):
    def __init__(self,*args,**kwargs):

        self.Desc = kwargs.pop('SDesc')

        super(ListForm,self).__init__(*args,**kwargs)

        
        queryset=Share.objects.values_list('describ','describ').order_by('describ').distinct()
        self.fields['ShareDescrib'] = forms.ChoiceField(widget=forms.Select(attrs={'onChange':'this.form.submit()'}),
        required=True,
        choices=[(o) for o in queryset])
        
        for i in range(0,int(queryset.count())):
            if self.fields['ShareDescrib'].choices[i][0]==self.Desc:
                self.initial['ShareDescrib'] = self.fields['ShareDescrib'].choices[i][0]
###################################################
#    ShareDescrib,initial={'ab': 'ab'}

def clean_name(self):
    name= self.cleaned_data.get('name')
    return name
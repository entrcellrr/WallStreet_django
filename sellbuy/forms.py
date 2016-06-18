# -*- coding: utf-8 -*-
from django import forms
from sellbuy.models import Share, ShareDetail
from login.models import UserDetail
from itertools import chain

class ShareForm(forms.ModelForm):
    class Meta:
        model=Share
        fields=['name','describ','currentprice']



class ListForm(forms.Form):
    def __init__(self,*args,**kwargs):

        self.Desc = kwargs.pop('SDesc')
        self.Sname = kwargs.pop('Sname')

        super(ListForm,self).__init__(*args,**kwargs)

        
        queryset=Share.objects.values_list('describ','describ').order_by('describ').distinct()
        #queryset = list(chain(queryset,tuple({tuple({u'all'})+tuple({u'all'})})))
        if self.Desc !='All':
            queryshares=Share.objects.values_list('name','name').order_by('name').filter(describ=self.Desc)
        else:
            queryshares=Share.objects.values_list('name','name').order_by('name').exclude(name='none')
    
        self.fields['ShareDescrib'] = forms.ChoiceField(widget=forms.Select(attrs={'onChange':'this.form.submit()'}),
        required=True,
        choices=[(o) for o in queryset])

        self.fields['ShareName'] = forms.ChoiceField(widget=forms.Select(attrs={'onChange':'this.form.submit()'}),
        required=True,
        choices=[(o) for o in queryshares])
        
        for i in range(0,int(queryset.count())):
            if self.fields['ShareDescrib'].choices[i][0]==self.Desc:
                self.initial['ShareDescrib'] = self.fields['ShareDescrib'].choices[i][0]
        if self.Sname is not None:
            for i in range(0,int(queryshares.count())):
                if self.fields['ShareName'].choices[i][0]==self.Sname:
                    self.initial['ShareName'] = self.fields['ShareName'].choices[i][0]  
###################################################
#    ShareDescrib,initial={'ab': 'ab'}
class Form_Calculated(forms.Form):
    QTY=forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs={'required':True, 'max_length':30}), label=("QTY"), error_messages={ 'invalid': ("This value must contain only letters, numbers and underscores.") })    
    current_price = forms.CharField(required=True)   
###################################################
#    ShareDescrib,initial={'ab': 'ab'}

def clean_name(self):
    name= self.cleaned_data.get('name')
    return name
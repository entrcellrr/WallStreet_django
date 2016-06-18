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
        self.UserName = kwargs.pop('UserName')
        super(ListForm,self).__init__(*args,**kwargs)

        queryset=Share.objects.values_list('describ','describ').order_by('describ').distinct()
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
        
        price=Share.objects.get(name=self.Sname)

        if self.Desc==price.describ or self.Desc=='All':
            var_crrntprice=price.currentprice
            qty = ShareDetail.objects.values_list(str(self.Sname)).filter(username=self.UserName)
            var_qty = qty[0][0]
        else:
            var_crrntprice=price.currentprice
            qty = ShareDetail.objects.values_list(str(self.fields['ShareName'].choices[0][0])).filter(username=self.UserName)
            var_qty = qty[0][0]
            qty = ShareDetail.objects.values_list(str(self.fields['ShareName'].choices[0][0])).filter(username=self.UserName)
            price=Share.objects.get(name=self.Sname)
            var_crrntprice=price.currentprice   

        self.fields['QTY']=forms.CharField(widget = forms.TextInput(attrs={'value':var_qty,
            'size':5,
            'title': 'Qty',
            'disabled':'disabled'}),required=True)    
    
        self.fields['Current_Price']=forms.IntegerField(widget = forms.TextInput(attrs={
            'value':var_crrntprice,
            'size': 5,
            'title': 'Currnt_price',
            'disabled':'disabled'
            }),required=True)
    
def clean_name(self):
    name= self.cleaned_data.get('name')
    return name
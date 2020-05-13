from django.db import models
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_txt','name','email')
        widgets = {
            'comment_txt': forms.Textarea (attrs= {'class':'form-control w-100', 'name':'comment','id':'comment' ,'cols':'30', 'rows':'9' , 'placeholder':'Write Comment'}),
            'name': forms.TextInput (attrs= {'class':'form-control', 'name':'name' ,'id':'name' ,'type':'text', 'placeholder':'Name'}),
            'email': forms.TextInput (attrs= {'class':'form-control' ,'name':'email', 'id':'email' ,'type':'email' ,'placeholder':'Email'}),
            
        }
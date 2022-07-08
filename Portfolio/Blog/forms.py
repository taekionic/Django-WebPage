from django.forms import ModelForm, forms, widgets
from django import forms
from .models import BlogTemplate, Comment
from django.db import models



class BlogPost(ModelForm):
    class Meta:
        model = BlogTemplate
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BlogPost, self).__init__(*args, **kwargs)
        self.fields['Title'].widget.attrs\
            .update({
                'class': 'bloginput'
        })
        self.fields['slug'].widget.attrs\
            .update({
                'class': 'bloginput',
        })
        self.fields['Author'].widget.attrs\
            .update({
                'class': 'bloginput'
        })
        self.fields['Category'].widget.attrs\
            .update({
                'class': 'bloginput'
        })
        self.fields['Body'].widget.attrs\
            .update({
                'class': 'bloginput'
        })
        self.fields['Status'].widget.attrs\
            .update({
                'class': 'bloginput'
        })


class Comments(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['post']

    def __init__(self, *args, **kwargs):
        super(Comments, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs\
            .update({
                'class': 'cominput'
        })
        self.fields['body'].widget.attrs\
            .update({
                'class': 'cominput'
        })
        self.fields['body'].widget.attrs\
            .update({
                'class': 'cominput'
        })


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, forms, widgets
from django import forms
from .models import Profile


class newUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self, commit=True):
        user = super(newUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(newUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs\
            .update({
                'class': 'reginputbox'
        })
        self.fields['email'].widget.attrs\
            .update({
                'class': 'reginputbox',
                'value': '',
        })
        self.fields['password1'].widget.attrs\
            .update({
                'class': 'reginputbox'
        })
        self.fields['password2'].widget.attrs\
            .update({
                'class': 'reginputbox'
        })

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
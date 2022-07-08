from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import newUserForm, ProfileForm
from .models import User, Profile




def Accounts(request):
    return render(request, 'accounthome.html')


def register_request(request):
    if request.user.is_authenticated:
        return redirect('PortfolioIndex')
    if request.method == "POST":
        form = newUserForm(request.POST, request.FILES)
        if request.method == 'POST':
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect('profile.html', )
    else:
        form = newUserForm()
        messages.error(request, "Please try again.")
    form = newUserForm()
    return render (request, "registration/register.html", {"register_form": form})



@login_required
def userprofile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'profile.html', context)

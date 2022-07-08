from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from Accounts import views


app_name = "Accounts"


urlpatterns = [
    path('', views.Accounts, name="accounthome"),
    path('register', views.register_request, name="register"),
    path('profile/<username>/', views.userprofile, name='profile'),
]

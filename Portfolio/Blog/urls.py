from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "Blog"

urlpatterns = [
    path('admin/', admin.site.urls),
    # blog urls
    path('', views.PostList, name='bloghome'),
    path('<slug:slug>/', views.PostDetail, name='post_page'),
    path('update/<slug:slug>', views.PostUpdate, name='postupdate'),
    path('delete/<slug:slug>', views.DeletePost, name='deletepost'),
    path('create', views.CreatePost, name='create')
]


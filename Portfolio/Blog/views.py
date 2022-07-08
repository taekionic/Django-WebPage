from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.template import loader
from .models import BlogTemplate, Comment
from .forms import BlogPost, Comments
from Portfolio.views import addInquiry
import requests
import json
from bs4 import BeautifulSoup

# Create your views here.
def PostList(request):
    context = (addInquiry(request))
    post = BlogTemplate.Post.all()
    post = BlogTemplate.Post.filter(Status=1).order_by('-Created_on')
    paginator = Paginator(post, 4)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    context.update(
        {'page': page,
        'count': paginator.count},
    )
    return render(request, 'bloghome.html', context)

def PostDetail(request, slug):
    view = BlogTemplate.Post.get(slug=slug)

    if request.method == 'POST':
        form = Comments(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post= view
            comment.save()
            return redirect('Blog:post_page', slug)
    else:
        form = Comments()

    context = {'view': view,
               'form': form,}
    return render(request, 'post_page.html', context)

def PostUpdate(request, slug):
    post = get_object_or_404(BlogTemplate, slug=slug)
    form = BlogPost(data=request.POST or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            formsave = form.save(commit=False)
            formsave.save()
            return redirect('Blog:post_page', slug)
    else:
        content = {
            'form': form,
            'post': post
        }
        return render(request, 'blogupdate.html', content)

def CreatePost(request):
    form = BlogPost(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Blog:bloghome')
        else:
            form = BlogPost()
            print(form.errors)
    return render(request, 'postcreate.html', context)

def DeletePost(request, slug):
    post = get_object_or_404(BlogTemplate, slug=slug)
    if request.method == 'POST':
        post.delete()
        # removing primary key value from url
        return redirect('Blog:bloghome')
    content = {'post': post}
    return render(request, 'blogdelete.html', content)






from django.db import models
from django.forms import TextInput, EmailInput
from django.contrib.auth.models import User


Blog_Status = [
    (0,"Draft/Private"),
    (1,"Publish"),
]

Blog_Category = [
    ('Coding', 'Coding'),
    ('Personal', 'Personal'),
    ('Career', 'Career'),
    ('Misc', 'Misc'),
]

class BlogTemplate(models.Model):
    Title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=30, unique=True, null=False)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    Category = models.CharField(max_length=100, choices=Blog_Category)
    Updated_on = models.DateTimeField(auto_now=True)
    Created_on = models.DateTimeField(auto_now_add=True)
    Body = models.TextField()
    Status = models.IntegerField(choices=Blog_Status, default=0)

    Post = models.Manager()

    class Meta:
        ordering = ['-Created_on']

    def __str__(self):
        return self.Title

class Comment(models.Model):
    post = models.ForeignKey(BlogTemplate, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    name = models.CharField(max_length=100)
    body = models.TextField(null=False, default="")
    date_added = models.DateTimeField(auto_now_add=True)

    Com = models.Manager()

    def __str__(self):
        return self.body
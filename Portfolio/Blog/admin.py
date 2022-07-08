from django.contrib import admin

# Register your models here.
from .models import BlogTemplate, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('Title', 'slug', 'Status','Created_on')
    list_filter = ("Status",)
    search_fields = ['title', 'Body']
    prepopulated_fields = {'slug': ('Title',)}

admin.site.register(BlogTemplate, PostAdmin)
admin.site.register(Comment)
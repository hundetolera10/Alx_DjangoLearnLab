from django.contrib import admin
from .models import post

admin.site.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content',)
    list_filter = ('published_date', 'author')
    

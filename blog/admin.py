from django.contrib import admin

# Register your models here.
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, requests, queryset):
        queryset.update(active=True)

admin.site.register(Post, PostAdmin)

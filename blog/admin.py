from django.contrib import admin

from .models import Post, Category, Comment

# Register your models here.
class CommentItemInline(admin.TabularInline):
     model = Comment
     raw_id_fields = ['post']
     # extra = 0

class PostAdmin(admin.ModelAdmin):
     search_fields = ['title', 'intro', 'body']
     list_display = ['title', 'slug', 'created_at', 'category']
     list_filter = ['created_at', 'category', 'status']
     inlines = [CommentItemInline]
     
class CategoryAdmin(admin.ModelAdmin):
     search_fields = ['title']
     list_display = ['title', 'slug']
     list_filter = ['title']

class CommentAdmin(admin.ModelAdmin):
     search_fields = ['name', 'email', 'body']
     list_display = ['name', 'email', 'body', 'created_at']
     list_filter = ['created_at']



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
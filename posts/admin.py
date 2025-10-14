from django.contrib import admin

#added line
from .models import Post, Comment, Repost, Filter

# admin modification
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class FilterInline(admin.TabularInline):
    model = Filter

class RepostAdmin(admin.ModelAdmin):
    list_display = ('post', 'date_added')

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_type', 'likes', 'post_time')
    inlines = [
        CommentInline,
        FilterInline,
    ]

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Repost, RepostAdmin)
admin.site.register(Comment)
admin.site.register(Filter)

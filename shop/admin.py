from django.contrib import admin
from .blog_post.models import BlogVideo ,BlogGallery,BlogAudio,Comment,Category

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','video','audio','gallery')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at','updated_at')

@admin.register(BlogVideo)
class BlogVideoAdmin(admin.ModelAdmin):
    list_display = ('id','title')

@admin.register(BlogGallery)
class BlogGalleryAdmin(admin.ModelAdmin):
    list_display = ('id','title','archived_at')

@admin.register(BlogAudio)
class BlogAudioAdmin(admin.ModelAdmin):
    list_display = ('id','title')

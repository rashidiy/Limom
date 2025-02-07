from django.contrib import admin
from .blog_post.models import BlogVideo ,BlogGallery,BlogAudio,Comments

admin.site.register(BlogGallery)
admin.site.register(BlogAudio)
admin.site.register(BlogVideo)
admin.site.register(Comments)

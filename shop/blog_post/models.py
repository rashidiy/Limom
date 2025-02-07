from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Comments(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.DateTimeField(auto_now=timezone.now())
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class BlogVideo(models.Model):
    blog_video_title = models.CharField(max_length=50)
    content=models.TextField()
    blog_video=models.FileField(upload_to='image/blog_post/blog_video')
    comment = models.ManyToManyField(Comments, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_video_title



class BlogGallery(models.Model):
    blog_gallery_title=models.CharField(max_length=50)
    content=models.TextField()
    blog_image = models.ImageField(upload_to='image/blog_gallery', null=True, blank=True)
    comment = models.ManyToManyField(Comments, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)



class BlogAudio(models.Model):
    blog_audio_title=models.CharField(max_length=50)
    content=models.TextField()
    blog_audio=models.FileField(upload_to='image/blog_post/blog_audio')
    comment = models.ManyToManyField(Comments, blank=True)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_audio_title






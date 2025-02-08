from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .validator import validate_archive_time


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class BlogVideo(models.Model):
    title = models.CharField(max_length=50)
    content=models.TextField()
    blog_video=models.FileField(upload_to='image/blog_post/blog_video')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archived_at = models.DateTimeField(null=True, blank=True,validators=[validate_archive_time])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_comment_count(self):
        """Galleryga nechta komment yozilganini qaytaradi"""
        return self.comments.count()


class BlogGallery(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    blog_image = models.ImageField(upload_to='image/blog_gallery', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    archived_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def is_archived(self):
        """Post 2 soniyadan keyin avtomatik arxivlangan bo‘lishi kerak"""
        if self.archived_at:
            return True  # Agar arxivlangan bo'lsa
        return now() >= self.created_at + timedelta(seconds=2)

    def get_comment_count(self):
        """Galleryga nechta komment yozilganini qaytaradi"""
        return self.comments.count()



class BlogAudio(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    blog_audio=models.FileField(upload_to='image/blog_post/blog_audio')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    archived_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_comment_count(self):
        """Galleryga nechta komment yozilganini qaytaradi"""
        return self.comments.count()



class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(BlogVideo, on_delete=models.CASCADE,null=True, blank=True , related_name="comments")
    audio = models.ForeignKey(BlogAudio, on_delete=models.CASCADE,null=True, blank=True, related_name="comments")
    gallery = models.ForeignKey(BlogGallery, on_delete=models.CASCADE,null=True, blank=True, related_name="comments")

    def __str__(self):
        return f"{self.name}{self.video}{self.audio},{self.gallery}"

    def get_comment_time(self):
        """Komment vaqtini formatlangan holda chiqarish"""
        return self.created_at.strftime("%Y-%m-%d %H:%M")







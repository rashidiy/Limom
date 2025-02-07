from django.shortcuts import render
from django.views import View
from .models import BlogAudio,BlogVideo,BlogGallery
from products.models.product.categories import Category



class BlogPost(View):
    def get(self,request):
        blog_audios=BlogAudio.objects.all()
        blog_videos=BlogVideo.objects.all()
        blog_gallerys=BlogGallery.objects.all()
        for i in blog_gallerys,blog_audios,blog_videos:
            if  i :
                context = {
                    'blog_audios': blog_audios,
                    'blog_videos': blog_videos,
                    'blog_gallerys': blog_gallerys,
                }
                return render(request, 'blog/blog-list.html', context)

            return render(request, 'pages/404.html', status=404)


class BlogAudioFormat(View):
    def get(self,request,id):
        categories=Category.objects.all()
        blog_audio_formats=BlogAudio.objects.get(id=id)
        context={
            'blog_audio_formats':blog_audio_formats,
            'categories':categories
        }
        return render(request,'blog/blog-audio-format.html',context)


class BlogVideoFormat(View):
    def get(self,request,id):
        categories = Category.objects.all()
        blog_video_formats=BlogVideo.objects.get(id=id)
        context={
            'blog_video_formats':blog_video_formats,
            'categories': categories
        }
        return render(request,'blog/blog-video-format.html',context)

class BlogGalleryFormat(View):
    def get(self, request, id):
        categories = Category.objects.all()
        blog_gallery_formats = BlogGallery.objects.get(id=id)
        context = {
            'blog_gallery_formats': blog_gallery_formats,
            'categories': categories
        }
        return render(request, 'blog/blog-gallery-format.html', context)


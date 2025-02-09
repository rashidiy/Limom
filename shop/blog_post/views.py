from django.shortcuts import render
from django.views import View
from .models import BlogAudio,BlogVideo,BlogGallery,Comment
from .models import Category
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm



class BlogPost(View):

    """ blog post qismini asosi qismida malumotlarni chiqarish uchun  """
    def get(self,request):
        categories = Category.objects.all().order_by('-id')     # Category  modeldan barcha malumotlarni oladi
        audios=BlogAudio.objects.all().order_by('-id')     # Blog Audio modeldan barcha malumotlarni oladi
        videos=BlogVideo.objects.all().order_by('-id')        # Blog Video  modeldan barcha malumotlarni oladi
        gallerys=BlogGallery.objects.all().order_by('-id')   # Blog Gallery  modeldan barcha malumotlarni oladi
        search = self.request.GET.get('search', '').strip()

        if search:
            videos = videos.filter(title__icontains=search)
            audios = audios.filter(title__icontains=search)
            gallerys=gallerys.filter(title__icontains=search)

        context = {
            'audios': audios,
            'videos': videos,
            'gallerys': gallerys,
            'categories': categories,
        }
        return render(request, 'blog/blog-left-sidebar3.html', context)




""" Blog Audio Detail Format """
class BlogAudioFormat(View):

    """ malumotlarni o'qib olish """
    def get(self,request,id):
        categories=Category.objects.all()
        latest_posts = BlogAudio.objects.order_by('-id')[:3]
        audios=BlogAudio.objects.get(id=id)
        comments = audios.comments.all().order_by('-id')
        context={
            'audios':audios,
            'categories':categories,
            'latest_posts':latest_posts,
            'comments':comments,
        }
        return render(request,'blog/blog-audio-format.html',context)

    """ blog audio postni commentarya qismi """
    def post(self,request,id):
        audios= BlogAudio.objects.get(id=id)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment=form.save(commit=False)
                comment.audio=audios
                comment.save()
                return redirect('shop:audio', id=audios.id)
        else:
            form = CommentForm()
        context = {
            'audios':audios,
            'form':form,
        }
        return render(request,'blog/blog-audio-format.html',context)






""" Blog Video Detail Format """
class BlogVideoFormat(View):

    """ malumotlarni korish """
    def get(self,request,id):
        categories = Category.objects.all()
        latest_posts = BlogVideo.objects.order_by('-id')[:3]
        videos=BlogVideo.objects.get(id=id)
        comments = videos.comments.all().order_by('-id')
        context={
            'videos':videos,
            'categories': categories,
            'latest_posts':latest_posts,
            'comments': comments,
        }
        return render(request,'blog/blog-video-format.html',context)

    """ blog video postni commenttarya qismi """
    def post(self, request, id):
        videos = BlogVideo.objects.get(id=id)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.video = videos
                comment.save()
                return redirect('shop:video',   id=videos.id)
        else:
            form = CommentForm()
        context = {
            'videos': videos,
            'form': form,
        }
        return render(request, 'blog/blog-video-format.html', context)






""" Blog Gallery Detail Format """
class BlogGalleryFormat(View):

    """ malumotlarni korish """
    def get(self, request, id):
        categories = Category.objects.all()
        latest_posts = BlogGallery.objects.order_by('-id')[:3]
        gallerys = BlogGallery.objects.get(id=id)
        comments = gallerys.comments.all().order_by('-id')
        context = {
            'gallerys': gallerys,
            'categories': categories,
            'latest_posts':latest_posts,
            'comments': comments,
        }
        return render(request, 'blog/blog-gallery-format.html', context)

    """ blog gallery postni commenttarya qismi """
    def post(self, request, id):
        gallers = BlogGallery.objects.get(id=id)

        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.gallery = gallers
                comment.save()
                return redirect('shop:gallery', id=gallers.id)

        else:
            form = CommentForm()

        context = {
            'gallers': gallers,
            'form': form,
        }

        return render(request, 'blog/blog-gallery-format.html', context)



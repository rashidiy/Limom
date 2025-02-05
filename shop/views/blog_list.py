from django.views.generic import TemplateView


class BlogListTemplateView(TemplateView):
    template_name = 'blog/blog-list.html'



class BlogPageTemplateView(TemplateView):
    template_name = 'blog/blog-2.html'  # Avval 'blog/blog-2-column.html' edi

class Blog3PageView(TemplateView):
    template_name = 'blog/blog-3-column.html'  # ✅ To‘g‘ri

class Blog4PageView(TemplateView):
    template_name = 'blog/blog-left-sidebar3.html'  # Avval 'blog/blog-left-sidebar.html' edi

class Blog5PageView(TemplateView):
    template_name = 'blog/blog-right-sidebar4.html'  # Avval 'blog/blog-right-sidebar.html' edi

class Blog6PageView(TemplateView):
    template_name = 'blog/blog-list-left-sidebar.html'

class Blog7PageView(TemplateView):
    template_name = 'blog/blog-list-right-sidebar.html'

class Blog8PageView(TemplateView):
    template_name = 'blog/blog-details-left-sidebar.html'

class Blog9PageView(TemplateView):
    template_name = 'blog/blog-details-right-sidebar.html'

class BlogAudiView(TemplateView):
    template_name = 'blog/blog-audio-format.html'

class BlogVideoView(TemplateView):
    template_name = 'blog/blog-video-format.html'

class BlogGalaryView(TemplateView):
    template_name = 'blog/blog-gallery-format.html'

from django.views.generic import TemplateView


class Blog2view(TemplateView):
    template_name = 'blog/blog-2-column.html'


class Blog3View(TemplateView):
    template_name = 'blog/blog-3-column.html'

class Blog4View(TemplateView):
    template_name = 'blog/blog-left-sidebar.html'

class Blog5View(TemplateView):
    template_name = 'blog/blog-right-sidebar.html'

class Bloglist(TemplateView):
    template_name = 'blog/blog-list.html'

class Bloglist2(TemplateView):
    template_name = 'blog/blog-list-left-sidebar.html'


class Bloglist3(TemplateView):
    template_name = 'blog/blog-list-right-sidebar.html'


class Blogdetailslist2(TemplateView):
    template_name = 'blog/blog-details-left-sidebar.html'


class Blogdetailslist(TemplateView):
    template_name = 'blog/blog-details-right-sidebar.html'




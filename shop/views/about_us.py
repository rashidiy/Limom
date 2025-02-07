from django.views.generic import TemplateView


class AboutUsTemplateView(TemplateView):
    template_name = 'about_us/about-us.html'

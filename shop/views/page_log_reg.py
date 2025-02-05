from django.views.generic import TemplateView

class ContactView(TemplateView):
    template_name = 'pages/contact.html'

class AboutView(TemplateView):
    template_name = 'pages/about-us.html'

class FaqView(TemplateView):
    template_name = 'pages/faq.html'

class ErrorView(TemplateView):
    template_name = 'pages/404.html'

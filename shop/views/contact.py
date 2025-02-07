from django.views.generic import TemplateView


class ContactTemplateView(TemplateView):
    template_name = 'contact/contact.html'

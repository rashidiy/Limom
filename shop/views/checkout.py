from django.views.generic import TemplateView

class CheckOutPageTemplateView(TemplateView):
    template_name = 'checkout/checkout.html'
from django.views.generic import TemplateView
from products.models import Category

class HomePageTemplateView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()  # Barcha kategoriyalarni yuborish
        return context

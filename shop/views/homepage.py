from django.views.generic import TemplateView
from products.models import Product, Category

class HomePageTemplateView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch product categories and lists
        context['new_arrivals'] = Product.objects.all().order_by('created_at')
        context['premium'] = Product.objects.all().order_by('-price')
        context['cheapest'] = Product.objects.all().order_by('price')

        # Handle potential missing categories gracefully
        context['laptops'] = Product.objects.filter(category=Category.objects.filter(name='Laptops').first())
        tv_category = Category.objects.filter(name__iexact='TV').first()
        audio_category = Category.objects.filter(name__iexact='Audio').first()
        context['tv_audios'] = Product.objects.filter(category__in=[tv_category, audio_category]) if tv_category or audio_category else []
        phone_category = Category.objects.filter(name='Phones').first()
        context['phones'] = Product.objects.filter(category=phone_category) if phone_category else []

        return context

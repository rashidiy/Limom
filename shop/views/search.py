from django.db.models import Q
from django.views.generic import ListView

from products.models import Product


class SearchProductsView(ListView):
    model = Product
    template_name = 'search-result.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        category = self.request.GET.get('category', 'all')

        products = Product.objects.all()

        if category != 'all':
            products = products.filter(category__name__iexact=category)

        if query:
            products = products.filter(
                Q(title__icontains=query) |
                Q(short_description__icontains=query) |
                Q(long_description__icontains=query) |
                Q(category__name__icontains=query)
            )

        return products

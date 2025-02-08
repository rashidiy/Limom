from django.views.generic import DetailView

from products.models import Product


class SingleProductNormalDetailView(DetailView):
    template_name = 'shop/single-product-tab-style-top.html'
    model = Product
    context_object_name = 'product'

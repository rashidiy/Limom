from django.shortcuts import get_object_or_404, render

from products.models import Product


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'shop/single-product-tab-style-top.html', {'product': product})

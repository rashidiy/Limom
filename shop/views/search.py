from django.db.models import Q
from django.shortcuts import render
from products.models import Product, categories

def search_products(request):
    query = request.GET.get('q', '').strip()
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(long_description__icontains=query)|
            Q(category__name__icontains=query)
        )


    print(f"Natijalar soni: {products.count()}")
    for product in products:
        print(product.title)  #

    context = {'products': products, 'query': query}
    return render(request, 'search-result.html', context)


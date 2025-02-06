from django.db.models import Q
from django.shortcuts import render
from products.models import Product, categories

def search_products(request):
    query = request.GET.get('q', '').strip()  # Foydalanuvchi qidirgan so'z
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(title__icontains=query) |  # Product sarlavhasi bo‘yicha qidirish
            Q(short_description__icontains=query) |  # Qisqa tavsifi bo‘yicha qidirish
            Q(long_description__icontains=query)|
            Q(category__name__icontains=query) # Uzun tavsifi bo‘yicha qidirish
        )


    print(f"Natijalar soni: {products.count()}")  # Terminalda natijalar sonini chiqaramiz
    for product in products:
        print(product.title)  # Har bir mahsulot nomini chiqaramiz

    context = {'products': products}
    return render(request, 'search_result.html', context)


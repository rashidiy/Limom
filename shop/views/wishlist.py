from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from products.models import Product, UserWishlist


class WishListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist/wishlist.html'
    context_object_name = 'wishlist_items'
    login_url = '/en/login/'  # Foydalanuvchi login qilmagan bo'lsa, ushbu sahifaga yo‘naltiriladi

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return []  # Agar login qilmagan bo‘lsa, bo‘sh ro‘yxat qaytariladi

        user_wishlist, created = UserWishlist.objects.get_or_create(user=self.request.user)
        return user_wishlist.wishlist.all()  # Faqat wishlist'dagi mahsulotlarni olish


@login_required(login_url="shop:login")
def add_wishlist(request):
    if request.method == 'POST':
        user = request.user
        product_id = request.POST.get('product_id')

        if not product_id:
            return JsonResponse({'error': 'Product ID required'}, status=400)

        product = get_object_or_404(Product, id=product_id)
        user_wishlist, created = UserWishlist.objects.get_or_create(user=user)

        if user_wishlist.wishlist.filter(id=product.id).exists():
            user_wishlist.wishlist.remove(product)
            added = False
        else:
            user_wishlist.wishlist.add(product)
            added = True

        return JsonResponse({'wishlist_count': user_wishlist.wishlist.count(), 'added': added})

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required(login_url="shop:login")
def remove_from_wishlist(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        if not product_id:
            return JsonResponse({"error": "Product ID required"}, status=400)

        product = get_object_or_404(Product, id=product_id)

        # UserWishlist modelidan wishlist olish
        user_wishlist, created = UserWishlist.objects.get_or_create(user=request.user)

        if user_wishlist.wishlist.filter(id=product.id).exists():
            user_wishlist.wishlist.remove(product)

        return JsonResponse({"wishlist_count": user_wishlist.wishlist.count()})

    return JsonResponse({"error": "Invalid request"}, status=400)


def wishlist_count(request):
    if request.user.is_authenticated:
        user_wishlist, _ = UserWishlist.objects.get_or_create(user=request.user)
        return {'wishlist_count': user_wishlist.wishlist.count()}
    return {'wishlist_count': 0}
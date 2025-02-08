from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from products.models import Product, UserWishlist


class WishListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist/wishlist.html'
    context_object_name = 'wishlist_items'
    login_url = '/en/login/'

    def get_queryset(self):
        user_wishlist, _ = UserWishlist.objects.get_or_create(user=self.request.user)
        return user_wishlist.wishlist.all()


@method_decorator(csrf_exempt, name='dispatch')
class AddToWishlistView(LoginRequiredMixin, View):
    login_url = "shop:login"

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        if not product_id:
            return JsonResponse({'error': 'Product ID required'}, status=400)

        product = get_object_or_404(Product, id=product_id)
        user_wishlist, _ = UserWishlist.objects.get_or_create(user=request.user)

        if user_wishlist.wishlist.filter(id=product.id).exists():
            user_wishlist.wishlist.remove(product)
            added = False
        else:
            user_wishlist.wishlist.add(product)
            added = True

        return JsonResponse({'wishlist_count': user_wishlist.wishlist.count(), 'added': added})


@method_decorator(csrf_exempt, name='dispatch')
class RemoveFromWishlistView(LoginRequiredMixin, View):
    login_url = "shop:login"

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        if not product_id:
            return JsonResponse({'error': 'Product ID required'}, status=400)

        product = get_object_or_404(Product, id=product_id)
        user_wishlist, _ = UserWishlist.objects.get_or_create(user=request.user)

        if user_wishlist.wishlist.filter(id=product.id).exists():
            user_wishlist.wishlist.remove(product)

        return JsonResponse({'wishlist_count': user_wishlist.wishlist.count()})
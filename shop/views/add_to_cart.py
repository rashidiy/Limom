from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
from products.models import Product
from products.models.add_tocart.modelsaddcart import UserCart




class CartListView(LoginRequiredMixin, ListView):
    template_name = 'shop/shopping-cart.html'
    context_object_name = 'cart_items'
    login_url = '/en/login/'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return []

        user_cart, created = UserCart.objects.get_or_create(user=self.request.user)
        return user_cart.cart.all()


@login_required(login_url="shop:login")
def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        product_id = request.POST.get('product_id')

        if not product_id:
            return JsonResponse({'error': 'Product ID required'}, status=400)

        product = get_object_or_404(Product, id=product_id)
        user_cart, created = UserCart.objects.get_or_create(user=user)

        if user_cart.cart.filter(id=product.id).exists():
            user_cart.cart.remove(product)
            added = False
        else:
            user_cart.cart.add(product)
            added = True

        return JsonResponse({'cart_count': user_cart.cart.count(), 'added': added})

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required(login_url="shop:login")
def remove_from_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        if not product_id:
            return JsonResponse({"error": "Product ID required"}, status=400)

        product = get_object_or_404(Product, id=product_id)

        user_cart, created = UserCart.objects.get_or_create(user=request.user)

        if user_cart.cart.filter(id=product.id).exists():
            user_cart.cart.remove(product)

        return JsonResponse({"cart_count": user_cart.cart.count()})

    return JsonResponse({"error": "Invalid request"}, status=400)


def cart_count(request):
    if request.user.is_authenticated:
        user_cart, _ = UserCart.objects.get_or_create(user=request.user)
        return {'cart_count': user_cart.cart.count()}
    return {'cart_count': 0}
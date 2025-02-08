from products.models import Category,UserWishlist
from products.models.add_tocart.modelsaddcart import UserCart

def cart_items(request):
    if request.user.is_authenticated:
        user_cart, _ = UserCart.objects.get_or_create(user=request.user)
        return {'cart_items': user_cart.cart.all(), 'cart_total': sum([p.price for p in user_cart.cart.all()])}
    return {'cart_items': [], 'cart_total': 0}


def categories(request):
    return {'categories': Category.objects.all()}


def wishlist_count(request):
    if request.user.is_authenticated:
        user_wishlist, _ = UserWishlist.objects.get_or_create(user=request.user)
        return {'wishlist_count': user_wishlist.wishlist.count()}
    return {'wishlist_count': 0}

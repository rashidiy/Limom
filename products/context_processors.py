from products.models import Category,UserWishlist


def categories(request):
    return {'categories': Category.objects.all()}


def wishlist_count(request):
    if request.user.is_authenticated:
        user_wishlist, _ = UserWishlist.objects.get_or_create(user=request.user)
        return {'wishlist_count': user_wishlist.wishlist.count()}
    return {'wishlist_count': 0}
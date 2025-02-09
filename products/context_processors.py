from products.models import Category, UserWishlist


def categories(request):
    return {'categories': Category.objects.all()}


def wishlist_count(request):
    user_wishlist = 0
    if request.user.is_authenticated:
        user_wishlist = UserWishlist.objects.filter(user=request.user).count()
    return {'wishlist_count': user_wishlist}

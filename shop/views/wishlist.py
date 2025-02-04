from django.views.generic import TemplateView, ListView

class WishListView(ListView):
    template_name = 'wishlist/wishlist.html'

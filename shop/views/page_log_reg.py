from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'pages/login-register.html'

class ChekView(TemplateView):
    template_name = 'pages/checkout.html'

class CompareView(TemplateView):
    template_name = 'pages/compare.html'

class WishlistView(TemplateView):
    template_name = 'pages/wishlist.html'

class ShopCartView(TemplateView):
    template_name = 'pages/shopping-cart.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'

class AboutView(TemplateView):
    template_name = 'pages/about-us.html'

class FaqView(TemplateView):
    template_name = 'pages/faq.html'

class ErrorView(TemplateView):
    template_name = 'pages/404.html'

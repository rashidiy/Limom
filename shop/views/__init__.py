from .about_us import AboutUsTemplateView
from .accessories import AccessoriesTemplateView
from .about_us import AboutUsTemplateView
from .blog_list import (Blog3PageView, Blog4PageView, Blog5PageView,
                        Blog6PageView, Blog7PageView, Blog8PageView,
                        Blog9PageView, BlogAudiView, BlogGalaryView,
                        BlogListTemplateView, BlogPageTemplateView,
                        BlogVideoView)
from .checkout import CheckOutPageTemplateView
from .compare import CompareTemplateView
from .contact import ContactTemplateView
from .error import custom_404_view, custom_500_view
from .contact import ContactTemplateView
from .homepage import HomePageTemplateView
from .login_register import LoginView,ForgotPasswordView,OTPView,SignupView,EditProfileView,LogoutView,UserChangeForm

from .page_log_reg import AboutView, ContactView, ErrorView, FaqView
from .product import SingleProductNormalDetailView,Product
from .shop import (Shop3PageTemplateView, Shop4PageTemplateView,
                   ShopListLeftSidebarPageTemplateView,
                   ShopListPageTemplateView,
                   ShopListRightSidebarPageTemplateView, ShopPageTemplateView,
                   ShoppingCardTemplateView, ShopRightSidebarPageTemplateView,

                   SingleProductSaleTemplateView,
                   SingleProductTabStyleTopTemplateView)

from .smartwatch import SmartwatchTemplateView
from shop.views.add_to_cart import add_to_cart,cart_count,remove_from_cart

# from .search import search_products
from shop.views.search import SearchProductsView
from .wishlist import WishListView,AddToWishlistView,RemoveFromWishlistView,UserWishlist
from .search import SearchProductsView

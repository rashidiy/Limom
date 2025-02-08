from django.urls import path
from shop.views import SearchProductsView
from shop.views.wishlist import WishListView,RemoveFromWishlistView,AddToWishlistView
from shop.views.error import custom_404_view,custom_500_view
from shop.views.product import SingleProductNormalDetailView
from shop.views.add_to_cart import cart_count, remove_from_cart, add_to_cart,CartListView

handler404 = custom_404_view



from shop.views import (HomePageTemplateView, ShopPageTemplateView, WishListView,
                        CheckOutPageTemplateView,
                        Shop3PageTemplateView, Shop4PageTemplateView, ShopRightSidebarPageTemplateView,
                        ShopListPageTemplateView, ShopListLeftSidebarPageTemplateView,
                        ShopListRightSidebarPageTemplateView,
                        SingleProductSaleTemplateView,
                        ShoppingCardTemplateView, CompareTemplateView,
                        LogoutView,
                        BlogPageTemplateView, Blog3PageView, Blog4PageView,
                        Blog5PageView, Blog6PageView, Blog7PageView,
                        Blog8PageView, Blog9PageView, BlogListTemplateView,
                        BlogVideoView, BlogAudiView, BlogGalaryView,
                        AboutUsTemplateView, ContactTemplateView, AccessoriesTemplateView, SmartwatchTemplateView,
                        FaqView, ErrorView,SignupView,OTPView,EditProfileView,ForgotPasswordView,LoginView
                        )
from shop.views.page_log_reg import ContactView,\
    AboutView, FaqView, ErrorView

app_name = 'shop'

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home'),
    path('blog1/', BlogListTemplateView.as_view(), name='blog1'),
    path('blog2/', BlogPageTemplateView.as_view(), name='blog2'),
    path('blog3/', Blog3PageView.as_view(), name='blog3'),
    path('blog4/', Blog4PageView.as_view(), name='blog4'),
    path('blog5/', Blog5PageView.as_view(), name='blog5'),
    path('blog6/', Blog6PageView.as_view(), name='blog6'),
    path('blog7/', Blog7PageView.as_view(), name='blog7'),
    path('blog8/', Blog8PageView.as_view(), name='blog8'),
    path('blog9/', Blog9PageView.as_view(), name='blog9'),
    path('blog10/', BlogAudiView.as_view(), name='blog10'),
    path('blog11/', BlogVideoView.as_view(), name='blog11'),
    path('blog12/', BlogGalaryView.as_view(), name='blog12'),
    path('page1', LoginView.as_view(), name='page1'),
    path('page6', ContactView.as_view(), name='page6'),
    path('page7', AboutView.as_view(), name='page7'),
    path('page8', FaqView.as_view(), name='page8'),
    path('page9', ErrorView.as_view(), name='page9'),
    path('shop/', ShopPageTemplateView.as_view(), name='shop'),
    path('shop3/', Shop3PageTemplateView.as_view(), name='shop3'),
    path('shop4/', Shop4PageTemplateView.as_view(), name='shop4'),
    path('shop/right-sidebar/', ShopRightSidebarPageTemplateView.as_view(), name='shopRightSidebar'),
    path('shop/shop-list/', ShopListPageTemplateView.as_view(), name='shopList'),
    path('shop/shopping-card/', ShoppingCardTemplateView.as_view(), name='shoppingCard'),
    path('compare/', CompareTemplateView.as_view(), name='compare'),
    path('shop/shop-list-left-sidebar/', ShopListLeftSidebarPageTemplateView.as_view(), name='shopListLeftSidebar'),
    path('shop/shop-list-right-sidebar/', ShopListRightSidebarPageTemplateView.as_view(), name='shopListRightSidebar'),
    path('single/product_sale/', SingleProductSaleTemplateView.as_view(), name='single_product_sale'),
    path('shop/product/detail/<int:pk>/', SingleProductNormalDetailView.as_view(), name='product_detail'),
    path('checkout/', CheckOutPageTemplateView.as_view(), name='checkout'),
    path('about-us', AboutUsTemplateView.as_view(), name='about_us'),
    path('about-us', ContactTemplateView.as_view(), name='contact'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('wishlist/add/', AddToWishlistView.as_view(), name='add_wishlist'),
    path('wishlist/remove/', RemoveFromWishlistView.as_view(), name='remove_wishlist'),
    path('register/', SignupView.as_view(), name='register'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('checkout/', CheckOutPageTemplateView.as_view(), name='checkout'),
    path('myprofile/', EditProfileView.as_view(), name='myprofile'),
    path('search/', SearchProductsView.as_view(), name='search'),
    path('otp/', OTPView.as_view(), name='otp'),
    path('cart/', CartListView.as_view(), name='cart_list'),
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/remove/', remove_from_cart, name='remove_from_cart'),
    path('cart/count/', cart_count, name='cart_count'),

]

# 404 xatolik uchun sozlash
handler404 = custom_404_view
handler500 = custom_500_view

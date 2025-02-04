from django.urls import path
from .views import (
    BlogPageTemplateView, Blog3PageView, Blog4PageView,
    Blog5PageView, Blog6PageView, Blog7PageView,
    Blog8PageView, Blog9PageView, BlogListTemplateView,
    BlogVideoView, BlogAudiView, BlogGalaryView,
)

from shop.views.page_log_reg import LoginView, ChekView, CompareView, WishlistView, ShopCartView, ContactView, \
    AboutView, FaqView, ErrorView

from shop.views.homepage import HomePageTemplateView

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
    path('page2', ChekView.as_view(), name='page2'),
    path('page3', CompareView.as_view(), name='page3'),
    path('page4', WishlistView.as_view(), name='page4'),
    path('page5', ShopCartView.as_view(), name='page5'),
    path('page6', ContactView.as_view(), name='page6'),
    path('page7', AboutView.as_view(), name='page7'),
    path('page8', FaqView.as_view(), name='page8'),
    path('page9', ErrorView.as_view(), name='page9'),
]


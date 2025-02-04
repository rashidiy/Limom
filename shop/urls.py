from django.urls import path

from shop.views import HomePageTemplateView

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home'),
]

from django.urls import path

from shop.views import HomePageTemplateView
from shop.blog import Blog3View, Blog4View, Blog5View, Blog2view,Bloglist,Bloglist2,Bloglist3,Blogdetailslist2,Blogdetailslist

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home'),
    path('blog2/', Blog2view.as_view(), name='blog2'),
    path('blog3/', Blog3View.as_view(), name='blog3'),
    path('blog4/', Blog4View.as_view(), name='blog4'),
    path('blog5/', Blog5View.as_view(), name='blog5'),
    path('bloglist/', Bloglist.as_view(), name='bloglist'),
    path('bloglist2/', Bloglist2.as_view(), name='bloglist2'),
    path('bloglist3/', Bloglist3.as_view(), name='bloglist3'),
    path('blogdetailslist/', Blogdetailslist2.as_view(), name='blogdetailslist2'),
    path('blogdetailslist/', Blogdetailslist.as_view(), name='blogdetailslist'),



]

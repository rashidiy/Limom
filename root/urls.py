from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + i18n_patterns(
    path('', include(('shop.urls', 'shop'), namespace='shop')),
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
)

path("ckeditor5/", include('django_ckeditor_5.urls')),

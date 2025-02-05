from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Product, Category, ProductImage, ProductDimension, ProductReview, ProductDiscount


class ProductAdminForm(forms.ModelForm):
    long_description = forms.CharField(widget=CKEditor5Widget)

    class Meta:
        model = Product
        fields = "__all__"


# ProductAdmin sinfini sozlash
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("title", "price", "category", "quantity", "seller")
    list_filter = ("category", "seller")
    search_fields = ("title", "short_description")
    ordering = ("-price",)
    fieldsets = (
        ('Asosiy Malumotlar', {
            'fields': ("title", "price", "category", "quantity", "seller", "short_description", "long_description")}),
        ('Uzbek', {'fields': ("title_uz", "short_description_uz", "long_description_uz")}),
        ('English', {'fields': ("title_en", "short_description_en", "long_description_en")}),
        ('Russian', {'fields': ("title_ru", "short_description_ru", "long_description_ru")}),

    )


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Asosiy Malumotlar', {
            'fields': ('name', 'parent')}),
        ('Uzbek', {'fields': ("name_uz",)}),
        ('English', {'fields': ("name_en",)}),
        ('Russian', {'fields': ("name_ru",)}),

    )


class ProductImageAdmin(admin.ModelAdmin):
    pass


class ProductDimensionAdmin(admin.ModelAdmin):
    pass


class ProductReviewAdmin(admin.ModelAdmin):
    pass


class ProductDiscountAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductDimension, ProductDimensionAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(ProductDiscount, ProductDiscountAdmin)

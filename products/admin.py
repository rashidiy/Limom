from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Product, Category, ProductImage, ProductDimension, ProductReview, ProductDiscount


class ProductAdminForm(forms.ModelForm):
    long_description = forms.CharField(widget=CKEditor5Widget)

    class Meta:
        model = Product
        fields = "__all__"


class ProductImagesTabular(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("title", "price", "category", "quantity", "seller")
    list_filter = ("category", "seller")
    search_fields = ("title", "short_description")
    ordering = ("-price",)
    inlines = (ProductImagesTabular,)
    fieldsets = (
        ('Asosiy Malumotlar', {
            'fields': ("title", "price", "category", "quantity", "seller", "short_description", "long_description")}),
        ('Uzbek', {'fields': ("title_uz", "short_description_uz", "long_description_uz")}),
        ('English', {'fields': ("title_en", "short_description_en", "long_description_en")}),
        ('Russian', {'fields': ("title_ru", "short_description_ru", "long_description_ru")}),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Asosiy Malumotlar', {
            'fields': ('name', 'parent')}),
        ('Uzbek', {'fields': ("name_uz",)}),
        ('English', {'fields': ("name_en",)}),
        ('Russian', {'fields': ("name_ru",)}),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductDimension)
class ProductDimensionAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    pass

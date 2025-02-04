from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Product, Category, ProductImage, ProductDimension, ProductReview, ProductDiscount

class ProductAdminForm(forms.ModelForm):
    long_description = forms.CharField(widget=CKEditorWidget())

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


class CategoryAdmin(admin.ModelAdmin):
    pass

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

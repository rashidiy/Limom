from django.contrib import admin

from products.models import (Product, Category,
                             ProductImage, ProductDimension,
                             ProductReview, ProductDiscount)


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

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

from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from products.models import Product, Category

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'shirt_description', 'long_description')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
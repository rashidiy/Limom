from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from products.models import Category, Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

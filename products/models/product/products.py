from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field


class Product(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    quantity = models.IntegerField(_('Quantity'), validators=[MinValueValidator(0)])
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE, related_name='products')
    seller = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='products')

    short_description = models.CharField(_('Short description'), max_length=2048)
    long_description = CKEditor5Field(_('Long description'), max_length=2048)  # todo: @thenodirjon CKeditorni qo'shish

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    @property
    def rating(self):
        return self.reviews.aggregate(average_rating=models.Avg('rate'))['average_rating']

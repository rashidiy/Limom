from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    quantity = models.IntegerField(_('Quantity  '), validators=[MinValueValidator(0)])
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE, related_name='products')
    seller = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    short_description = models.CharField(_('Short description'), max_length=2048)
    long_description = CKEditor5Field(_('Long description'), max_length=2048)  # todo: @thenodirjon CKeditorni qo'shish

    def get_absolute_url(self):
        return reverse('shop:shop_single_product_detail', kwargs={'pk': self.pk})

    def get_first_image(self):
        first_image = self.images.first()
        if first_image:
            return first_image.image.url
        return None

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('id',)

    def rating(self):
        avg_rating = self.reviews.aggregate(Avg('rate'))['rate__avg'] or 0  # Agar None bo'lsa, 0 oling
        return round(avg_rating, 1)


    def __str__(self):
        return f"{self.title} by {self.seller.username}"
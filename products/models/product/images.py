from django.db import models
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _

class ProductImage(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='images')
    image = ResizedImageField(size=[300, 300], crop=['middle', 'center'],  upload_to='products/images')

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')

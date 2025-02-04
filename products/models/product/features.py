from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductDimension(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    width = models.FloatField(_('Width'),blank=True)
    height = models.FloatField(_('Height'),blank=True)

    class Meta:
        verbose_name = _('Product Dimension')
        verbose_name_plural = _('Product Dimensions')

from django.db import models
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _

class ProductDiscount(models.Model):
    banner = ResizedImageField(_('Banner'))
    class Meta:
        verbose_name = _('Product Discount')
        verbose_name_plural = _('Product Discounts')
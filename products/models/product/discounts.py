from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField


class ProductDiscount(models.Model):
    banner = ResizedImageField(_('Banner'))
    class Meta:
        verbose_name = _('Product Discount')
        verbose_name_plural = _('Product Discounts')
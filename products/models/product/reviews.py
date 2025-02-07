from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductReview(models.Model):
    description = models.TextField(_('Description'), blank=True)
    name = models.CharField(_('Name'), max_length=255)
    email = models.EmailField(_('Email'), blank=True)
    rate = models.IntegerField( _('Rate'), validators=[MinValueValidator(0), MaxValueValidator(5)])

    product = models.ForeignKey('products.Product',  on_delete=models.RESTRICT, related_name='reviews')

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
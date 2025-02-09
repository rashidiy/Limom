from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductReview(models.Model):
    description = models.TextField(_('Description'), blank=True)
    name = models.CharField(_('Name'), max_length=255)
    email = models.EmailField(_('Email'), blank=True)
    rate = models.IntegerField(_('Rate'), validators=[MinValueValidator(1), MaxValueValidator(5)])
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='reviews', related_query_name='review')

    created_at = models.DateTimeField(auto_now_add=True)  # Qo‘shilgan vaqtni saqlash

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
        ordering = ['-created_at']  # Eng yangi sharhlarni birinchi ko‘rsatish

    def __str__(self):
        return f"{self.name} ({self.rate}★) - Product ID: {self.product_id}"


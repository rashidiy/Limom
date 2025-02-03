from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ProductReview(models.Model):
    description = models.TextField(blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    product = models.ForeignKey('products.Product', on_delete=models.RESTRICT, related_name='reviews')

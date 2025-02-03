from django.db import models


class ProductDimension(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    width = models.FloatField(blank=True)
    height = models.FloatField(blank=True)

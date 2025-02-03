from django.db import models
from django_resized import ResizedImageField


class ProductDiscount(models.Model):
    banner = ResizedImageField()
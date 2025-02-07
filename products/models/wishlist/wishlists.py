from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class UserWishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wishlist = models.ManyToManyField(Product)  # ManyToMany bo'lishi kerak

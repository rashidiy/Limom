from django.contrib.auth.models import User

from django.db import models
from products.models import Product


class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Product)
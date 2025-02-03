from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE, related_name='products')
    seller = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='products')

    short_description = models.CharField(max_length=2048)
    long_description = models.CharField(max_length=2048)  # todo: @thenodirjon CKeditorni qo'shish

    @property
    def rating(self):
        return self.reviews.aggregate(average_rating=models.Avg('rate'))['average_rating']

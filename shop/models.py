from django.contrib.auth.models import User
from django.db import models
from products.models import Product
from products.models.add_tocart.modelsaddcart import UserCart



class Order(models.Model):
    COUNTRY = [
        ('uz', 'Uzbekistan'),
        ('us', 'United States'),
        ('gb', 'United Kingdom'),
        ('ca', 'Canada'),
        ('de', 'Germany'),
        ('fr', 'France'),
        ('it', 'Italy'),
        ('es', 'Spain'),
        ('au', 'Australia'),
        ('jp', 'Japan'),
        ('cn', 'China'),
        ('ru', 'Russia'),
        ('in', 'India'),
        ('br', 'Brazil'),
        ('mx', 'Mexico'),
        ('tr', 'Turkey'),
        ('ae', 'United Arab Emirates'),
        ('za', 'South Africa'),
        ('kr', 'South Korea'),
        ('sa', 'Saudi Arabia'),
    ]

    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    apartment = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)  # O'zgartirish mumkin
    country = models.CharField(max_length=20, choices=COUNTRY, default='uz')
    order_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.first_name} {self.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.title} ({self.quantity})"

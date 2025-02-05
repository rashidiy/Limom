import random
from django.core.management.base import BaseCommand
from faker import Faker
from products.models.product.discounts import ProductDiscount

fake = Faker()

class Command(BaseCommand):
    help = "Creates fake product discounts"

    def handle(self, *args, **kwargs):
        for _ in range(50):
            banner_url = fake.image_url()


            ProductDiscount.objects.create(banner=banner_url)

        self.stdout.write(self.style.SUCCESS("Successfully created 10 product discounts"))

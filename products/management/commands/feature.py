import random
from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Product
from products.models.product.features import ProductDimension

fake = Faker()


class Command(BaseCommand):
    help = "Creates fake product dimensions"

    def handle(self, *args, **kwargs):
        products = list(Product.objects.all())

        if not products:
            self.stdout.write(self.style.ERROR("No products found! Please create some products first."))
            return

        for _ in range(50):
            product = random.choice(products)
            width = round(fake.random.uniform(5.0, 100.0), 2)
            height = round(fake.random.uniform(20.0, 200.0), 2)


            ProductDimension.objects.create(product=product, width=width, height=height)

        self.stdout.write(self.style.SUCCESS("Successfully created 10 product dimensions"))

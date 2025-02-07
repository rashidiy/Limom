import random

from django.core.management.base import BaseCommand
from faker import Faker

from products.models import Product, ProductDimension

fake = Faker()


class Command(BaseCommand):
    help = "Creates fake product dimensions"

    def add_arguments(self, parser):
        parser.add_argument(
            "count",
            type=int,
            nargs="?",
            default=50,
            help="Number of product dimensions to generate",
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        products = list(Product.objects.all())

        if not products:
            self.stdout.write(self.style.ERROR("⚠ No products found! Please create some products first."))
            return

        if count > len(products):
            count = len(products)  # Agar `count` mahsulot sonidan ko‘p bo‘lsa, maksimal mahsulot sonini ishlatamiz

        selected_products = random.sample(products, count)  # Tasodifiy `count` ta mahsulot tanlanadi

        for product in selected_products:
            width = round(random.uniform(5.0, 100.0), 2)
            height = round(random.uniform(20.0, 200.0), 2)

            ProductDimension.objects.create(product=product, width=width, height=height)

        self.stdout.write(self.style.SUCCESS(f"🎉 Successfully created {count} product dimensions!"))

import random
from django.core.management.base import BaseCommand
from faker import Faker
from products.models.product.reviews import ProductReview
from products.models.product.products import Product

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake product reviews using Faker"

    def add_arguments(self, parser):
        parser.add_argument(
            "count",
            type=int,
            nargs="?",
            default=50,
            help="Number of reviews to generate",
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        products = list(Product.objects.all())  # Ro‘yxatga o‘girish

        if not products:
            self.stdout.write(self.style.ERROR("No products found in the database."))
            return

        for _ in range(count):
            description = fake.text(max_nb_chars=200)
            name = fake.name()
            email = fake.email()
            rate = random.randint(0, 5)  # 0 dan 5 gacha reyting
            product = random.choice(products)  # Har bir sharh uchun mahsulotni tasodifiy tanlash

            ProductReview.objects.create(
                description=description,
                name=name,
                email=email,
                rate=rate,
                product=product,
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully generated {count} fake reviews."))

import random

from django.core.management.base import BaseCommand
from faker import Faker
from products.models.product.reviews import ProductReview
from products.models.product.products import Product


class Command(BaseCommand):
    help = 'Generate fake product reviews using Faker'

    def handle(self, *args, **kwargs):
        fake = Faker()


        products = Product.objects.all()

        if not products:
            self.stdout.write(self.style.ERROR('No product found in the database.'))
            return
        product = random.choice(products)


        for _ in range(50):
            description = fake.text(max_nb_chars=200)
            name = fake.name()
            email = fake.email()
            rate = fake.random_int(min=0, max=5)


            ProductReview.objects.create(
                description=description,
                name=name,
                email=email,
                rate=rate,
                product=product
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated 10 fake reviews for product "{}".'.format(product.title)))

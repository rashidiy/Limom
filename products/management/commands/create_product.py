import random
from faker import Faker
from django.core.management.base import BaseCommand
from products.models.product.products import Product
from products.models.product.categories import Category
from django.contrib.auth.models import User

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake products"

    def handle(self, *args, **kwargs):
        categories = list(Category.objects.all())
        users = list(User.objects.all())

        if not categories or not users:
            self.stdout.write(self.style.ERROR("Error: No categories or users found!"))
            return

        for _ in range(50):
            Product.objects.create(
                title=fake.sentence(nb_words=3),
                price=round(random.uniform(10, 500), 2),
                quantity=random.randint(1, 50),
                category=random.choice(categories),
                seller=random.choice(users),
                short_description=fake.text(max_nb_chars=100),
                long_description=fake.text(max_nb_chars=500)
            )

        self.stdout.write(self.style.SUCCESS("Successfully added fake products!"))

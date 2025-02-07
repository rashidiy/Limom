import random
from django.core.management.base import BaseCommand
from faker import Faker
from products.models.product.categories import Category

fake = Faker()


class Command(BaseCommand):
    help = "Creates fake categories"

    def handle(self, *args, **kwargs):
        categories = []

        for _ in range(50):
            name = fake.word().capitalize()
            parent = random.choice(categories) if categories and random.random() > 0.5 else None

            category = Category.objects.create(name=name, parent=parent)
            categories.append(category)

        self.stdout.write(self.style.SUCCESS("Successfully created 10 categories"))

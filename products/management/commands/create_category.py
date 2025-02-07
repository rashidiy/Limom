import random
from django.core.management.base import BaseCommand
from faker import Faker
from products.models.product.categories import Category

fake = Faker()

class Command(BaseCommand):
    help = "Creates fake categories"

    def add_arguments(self, parser):
        parser.add_argument(
            "count",
            type=int,
            nargs="?",
            default=50,
            help="Number of categories to generate",
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        categories = []

        for _ in range(count):
            name = fake.word().capitalize()
            parent = random.choice(categories) if categories and random.random() > 0.5 else None

            category = Category.objects.create(name=name, parent=parent)
            categories.append(category)

        self.stdout.write(self.style.SUCCESS(f"🎉 Successfully created {count} categories!"))

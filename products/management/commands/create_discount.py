from django.core.management.base import BaseCommand
from faker import Faker

from products.models.product.discounts import ProductDiscount

fake = Faker()


class Command(BaseCommand):
    help = "Creates fake product discounts"

    def add_arguments(self, parser):
        parser.add_argument(
            "count",
            type=int,
            nargs="?",
            default=50,
            help="Number of product discounts to generate",
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]

        for _ in range(count):
            banner_url = fake.image_url()

            ProductDiscount.objects.create(banner=banner_url)

        self.stdout.write(self.style.SUCCESS(f"🎉 Successfully created {count} product discounts!"))

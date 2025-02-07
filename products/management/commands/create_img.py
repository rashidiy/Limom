import os
import random
from django.core.management.base import BaseCommand
from products.models.product.products import Product
from products.models.product.images import ProductImage
from root.settings import BASE_DIR


class Command(BaseCommand):
    help = "Assign random images to existing products"

    def add_arguments(self, parser):
        parser.add_argument(
            "count",
            type=int,
            nargs="?",
            default=None,
            help="Number of products to assign images to",
        )

    def handle(self, *args, **kwargs):
        img_dir = os.path.join(BASE_DIR, "media/products/images/")
        img_files = [f for f in os.listdir(img_dir) if f.endswith((".jpg", ".png", ".jpeg"))]

        if not img_files:
            self.stdout.write(self.style.WARNING("⚠ No images found in media/products/images/"))
            return

        products = list(Product.objects.all())

        if not products:
            self.stdout.write(self.style.WARNING("⚠ No products found in the database!"))
            return

        count = kwargs["count"]
        if count is None or count > len(products):
            count = len(products)

        selected_products = random.sample(products, count)
        assigned_count = 0

        for product in selected_products:
            img_file = random.choice(img_files)
            img_path = os.path.join("products/images", img_file)

            ProductImage.objects.create(product=product, image=img_path)
            self.stdout.write(self.style.SUCCESS(f"✅ {img_file} assigned to product {product.title}!"))
            assigned_count += 1

        self.stdout.write(self.style.SUCCESS(f"🎉 Successfully assigned images to {assigned_count} products!"))

import os
import random
from django.core.management.base import BaseCommand
from products.models.product.products import Product
from products.models.product.images import ProductImage
from root.settings import BASE_DIR


class Command(BaseCommand):
    help = "Assign random images to existing products"

    def handle(self, *args, **kwargs):
        img_dir = os.path.join(BASE_DIR, 'media/products/images/')
        img_files = [f for f in os.listdir(img_dir) if f.endswith((".jpg", ".png", ".jpeg"))]

        if not img_files:
            self.stdout.write(self.style.WARNING("No images found!"))
            return

        products = list(Product.objects.all())

        if not products:
            self.stdout.write(self.style.WARNING("No products found!"))
            return

        count = 0
        for product in products:
            img_file = random.choice(img_files)
            
            img_path = os.path.join("products/images", img_file)

            ProductImage.objects.create(product=product, image=img_path)
            self.stdout.write(self.style.SUCCESS(f"✅ {img_file} assigned to product {product.title}!"))
            count += 1

        self.stdout.write(self.style.SUCCESS(f"Total {count} images assigned."))

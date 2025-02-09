from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from products.models.add_tocart.modelsaddcart import UserCart
from shop.forms import CheckoutForm
from shop.models import OrderItem
from django.contrib.auth import authenticate, login
from django.contrib import messages


class CheckOutPageTemplateView(View):
    template_name = "checkout/checkout.html"
    success_url = reverse_lazy("shop:order_success")

    def get(self, request, *args, **kwargs):
        """Foydalanuvchining savatidagi mahsulotlarni olish va formani ko‘rsatish"""
        if not request.user.is_authenticated:
            return redirect("shop:login")  # Login qilmagan bo‘lsa, login sahifasiga yo‘naltiramiz

        user_cart, created = UserCart.objects.get_or_create(user=request.user)

        # 🔴 Agar foydalanuvchining savati bo‘sh bo‘lsa, uni shop sahifasiga yo‘naltiramiz
        if not user_cart.cart.exists():
            messages.warning(request, "Sizning savatingiz bo‘sh! Avval mahsulot qo‘shing.")
            return redirect("shop:shop")  # shop sahifasiga qaytarish

        form = CheckoutForm()
        context = {
            "form": form,
            "cart_items": user_cart.cart.all(),
            "cart_total": sum(product.price for product in user_cart.cart.all())
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """Foydalanuvchi checkout formasini jo‘natganda buyurtma yaratish"""
        if not request.user.is_authenticated:
            return redirect("shop:login")

        user_cart, created = UserCart.objects.get_or_create(user=request.user)
        if not user_cart.cart.exists():
            return render(request, self.template_name, {
                "form": CheckoutForm(),
                "cart_items": user_cart.cart.all(),
                "cart_total": 0,
                "error": "Savat bo'sh! Iltimos, mahsulot qo'shing."
            })

        form = CheckoutForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            # UserCart'dagi mahsulotlarni OrderItem'ga o'tkazish
            for product in user_cart.cart.all():
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=1,  # Har bir mahsulotdan 1 dona qabul qilinmoqda
                    price=product.price
                )

            # Savatni tozalash
            user_cart.cart.clear()

            return redirect(self.success_url)

        return render(request, self.template_name, {
            "form": form,
            "cart_items": user_cart.cart.all(),
            "cart_total": sum(product.price for product in user_cart.cart.all())
        })

class OrderSuccessTemplateView(TemplateView):
    """foydalanuvchi Plase-order bosilganda unga xabar berish va asosiy sahifaga yunaltirish"""
    template_name = "checkout/order_success.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

from django.contrib import admin
from shop.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):  # OrderItem uchun Inline admin
    model = OrderItem
    extra = 0  # Qo‘shimcha bo‘sh qatordan qochish
    readonly_fields = ('product', 'quantity', 'price')
    can_delete = False  # Buyurtma ichidagi mahsulotni admin paneldan o‘chirishni oldini oladi


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone','created_at')
    list_filter = ('created_at', 'country')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    fieldsets = (
        ("Basic Information", {
            "fields": ("first_name", "last_name", "email", "phone", "company_name")
        }),
        ("Address Details", {
            "fields": ("address", "apartment", "city", "state", "postal_code", "country")
        }),
        ("Order Details", {
            "fields": ("order_notes", "created_at",)
        }),
    )

    inlines = [OrderItemInline]  # Order ichida mahsulotlarni ko‘rsatish uchun


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):  # OrderItem alohida ham ko‘rinadigan bo‘lishi uchun
    list_display = ('order', 'product', 'quantity', 'price')
    list_filter = ('order', 'product')
    search_fields = ('order__id', 'product__name')


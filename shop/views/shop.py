from django.core.paginator import Paginator
from django.db.models import Avg
from django.views.generic import TemplateView, ListView
from products.models import Product, Category


class ShopPageTemplateView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 12
    template_name = 'shop/shop-left-sidebar.html'

    # filter
    def get_queryset(self):
        products = Product.objects.all()
        category_id = self.request.GET.get('category')
        sort_option = self.request.GET.get('sort', 'relevance')
        if category_id:
            products = products.filter(category_id=category_id)
            # Saralash (sort by)
        elif sort_option == 'name_asc':
            products = products.order_by('title')
        elif sort_option == 'name_desc':
            products = products.order_by('-title')
        elif sort_option == 'price_low_high':
            products = products.order_by('price')
        elif sort_option == 'price_high_low':
            products = products.order_by('-price')
        elif sort_option == 'rating_lowest':
            products = products.annotate(avg_rating=Avg('reviews__rate')).order_by('avg_rating')
        elif sort_option == 'rating_highest':
            products = products.annotate(avg_rating=Avg('reviews__rate')).order_by('-avg_rating')

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()
        paginator = Paginator(products, 12)  # 12 ta mahsulot per page
        page = self.request.GET.get('page')
        products_paginated = paginator.get_page(page)

        context['products'] = products_paginated
        context['categories'] = Category.objects.all()
        context['sort_options'] = [
            ('relevance', 'Relevance'),
            ('name_asc', 'Name (A - Z)'),
            ('name_desc', 'Name (Z - A)'),
            ('price_low_high', 'Price (Low > High)'),
            ('price_high_low', 'Price (High > Low)'),
            ('rating_lowest', 'Rating (Lowest)'),
            ('rating_highest', 'Rating (Highest)'),
        ]
        return context

class SingleProductGroupTemplateView(TemplateView):
    template_name = 'shop/single-product-group.html'

class SingleProductTemplateView(TemplateView):
    template_name = 'shop/single-product.html'

class SingleProductSaleTemplateView(TemplateView):
    template_name = 'shop/single-product-sale.html'

class SingleProductNormalTemplateView(TemplateView):
    template_name = 'shop/single-product.html'

class SingleProductAffinityTemplateView(TemplateView):
    template_name = 'shop/single-product-affiliate.html'

class Shop3PageTemplateView(TemplateView):
    template_name = 'shop/shop-3-column.html'

class Shop4PageTemplateView(TemplateView):
    template_name = 'shop/shop-4-column.html'

class ShopRightSidebarPageTemplateView(TemplateView):
    template_name = 'shop/shop-right-sidebar.html'

class ShopListPageTemplateView(TemplateView):
    template_name = 'shop/shop-list.html'

class ShopListLeftSidebarPageTemplateView(TemplateView):
    template_name = 'shop/shop-left-sidebar.html'

class ShopListRightSidebarPageTemplateView(TemplateView):
    template_name = 'shop/shop-right-sidebar.html'

class SingleProductGalleryLeftTemplateView(TemplateView):
    template_name = 'shop/single-product-gallery-left.html'

class SingleProductCarouselTemplateView(TemplateView):
    template_name = 'shop/single-product-carousel.html'

class SingleProductGalleryRightTemplateView(TemplateView):
    template_name = 'shop/single-product-gallery-right.html'

class SingleProductTabStyleTopTemplateView(TemplateView):
    template_name = 'shop/single-product-tab-style-top.html'

class SingleProductTabStyleLeftTemplateView(TemplateView):
    template_name = 'shop/single-product-tab-style-left.html'

class SingleProductTabStyleRightTemplateView(TemplateView):
    template_name = 'shop/single-product-tab-style-right.html'

class ShoppingCardTemplateView(TemplateView):
    template_name = 'shop/shopping-cart.html'
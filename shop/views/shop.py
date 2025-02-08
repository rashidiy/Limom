from django.db.models import Avg, Count
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from products.models import Product, Category, ProductDimension


class ShopPageTemplateView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 12
    template_name = 'shop/shop-left-sidebar.html'

    # filter
    def get_queryset(self):
        products = Product.objects.all()
        category_id = self.request.GET.get('category')
        color = self.request.GET.get('color')
        size = self.request.GET.get('size')
        sort_option = self.request.GET.get('sort')
        dimensions = self.request.GET.getlist('dimension')

        filters = Q()
        if category_id:
            filters &= Q(category_id=category_id)
        if color:
            filters &= Q(dimensions__color=color)
        if size:
            filters &= Q(dimensions__size=size)

        if dimensions:
            dim_filters = Q()
            for dim in dimensions:
                try:
                    width, height = map(lambda x: float(x.replace(',', '.')) if ',' in x or '.' in x else int(x),
                                        dim.split('x'))
                    dim_filters |= Q(dimensions__width=width, dimensions__height=height)
                except ValueError:
                    continue
            filters &= dim_filters

        products = products.filter(filters).distinct()

        sort_options = {
            'name_asc': 'title',
            'name_desc': '-title',
            'price_low_high': 'price',
            'price_high_low': '-price',
            'rating_lowest': 'avg_rating',
            'rating_highest': '-avg_rating'
        }

        if sort_option in sort_options:
            if 'rating' in sort_option:
                products = products.annotate(avg_rating=Avg('reviews__rate')).order_by(sort_options[sort_option])
            else:
                products = products.order_by(sort_options[sort_option])

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_dimension_size'] = ProductDimension.objects.values('size').annotate(
            total=Count('size')).distinct()
        context['products_dimension_color'] = ProductDimension.objects.values('color').annotate(
            total=Count('color')).distinct()
        context['products_dimension_width'] = (
            ProductDimension.objects.values('width', 'height').annotate(total=Count('id')).distinct())
        context['categories'] = Category.objects.all()
        context['sort_options'] = [
            ('relevance', 'Relevance'),
            ('name_asc', 'Name (A - Z)'),
            ('name_desc', 'Name (Z - A)'),
            ('price_low_high', 'Price (Low > High)'),
            ('price_high_low', 'Price (High > Low)'),
            ('rating_lowest', 'Rating (Lowest)'),
            ('rating_highest', 'Rating (Highest)')
        ]
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            context['is_ajax'] = True  # AJAX so‘rov ekanligini tekshirish uchun
            return render(self.request, 'shop/includes/product_grid.html', context)
        return super().render_to_response(context, **response_kwargs)


class SingleProductSaleTemplateView(TemplateView):
    template_name = 'shop/single-product-sale.html'


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


class SingleProductTabStyleTopTemplateView(TemplateView):
    template_name = 'shop/single-product-tab-style-top.html'


class ShoppingCardTemplateView(TemplateView):
    template_name = 'shop/shopping-cart.html'

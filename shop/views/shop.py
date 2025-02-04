from django.views.generic import TemplateView


class ShopPageTemplateView(TemplateView):
    template_name = 'shop/shop-left-sidebar.html'

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
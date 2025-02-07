# from .about_us import AboutUsTemplateView
# from .accessories import AccessoriesTemplateView

from .checkout import *
from .checkout import CheckOutPageTemplateView
from .compare import *

from .compare import CompareTemplateView
# from .contact import ContactTemplateView
from .homepage import *
from .homepage import HomePageTemplateView
from .login_register import *
from .page_log_reg import (
    ContactView,
    AboutView,
    FaqView,
    ErrorView)
from .page_log_reg import ContactView, AboutView, FaqView, ErrorView
from .shop import *
from .shop import (ShopPageTemplateView, SingleProductTabStyleLeftTemplateView, SingleProductGroupTemplateView,
                   SingleProductNormalTemplateView, SingleProductTemplateView, SingleProductSaleTemplateView,
                   SingleProductAffinityTemplateView, Shop3PageTemplateView, Shop4PageTemplateView,
                   ShopRightSidebarPageTemplateView, ShopListPageTemplateView, ShopListPageTemplateView,
                   ShopListLeftSidebarPageTemplateView, ShopListRightSidebarPageTemplateView,
                   SingleProductGalleryLeftTemplateView, SingleProductCarouselTemplateView,
                   SingleProductGalleryRightTemplateView,
                   SingleProductTabStyleTopTemplateView, SingleProductTabStyleRightTemplateView,
                   ShoppingCardTemplateView
                   )
# from .smartwatch import SmartwatchTemplateView
from .wishlist import WishListView
# from .search import search_products

from .checkout import CheckOutPageTemplateView
from .compare import CompareTemplateView

from .error import custom_404_view
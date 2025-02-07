from .about_us import AboutUsTemplateView
from .accessories import AccessoriesTemplateView
from .about_us import AboutUsTemplateView
from .blog_list import (Blog3PageView, Blog4PageView, Blog5PageView,
                        Blog6PageView, Blog7PageView, Blog8PageView,
                        Blog9PageView, BlogAudiView, BlogGalaryView,
                        BlogListTemplateView, BlogPageTemplateView,
                        BlogVideoView)
from .checkout import *
from .checkout import CheckOutPageTemplateView
from .compare import *
from .compare import CompareTemplateView
from .contact import ContactTemplateView
from .error import custom_404_view
# from .contact import ContactTemplateView
from .homepage import *
from .homepage import HomePageTemplateView

from .login_register import *
from .page_log_reg import AboutView, ContactView, ErrorView, FaqView
from .search import *
from .shop import *
from .shop import (Shop3PageTemplateView, Shop4PageTemplateView,
                   ShopListLeftSidebarPageTemplateView,
                   ShopListPageTemplateView,
                   ShopListRightSidebarPageTemplateView, ShopPageTemplateView,
                   ShoppingCardTemplateView, ShopRightSidebarPageTemplateView,
                   SingleProductAffinityTemplateView,
                   SingleProductCarouselTemplateView,
                   SingleProductGalleryLeftTemplateView,
                   SingleProductGalleryRightTemplateView,
                   SingleProductGroupTemplateView,
                   SingleProductNormalTemplateView,
                   SingleProductSaleTemplateView,
                   SingleProductTabStyleLeftTemplateView,
                   SingleProductTabStyleRightTemplateView,
                   SingleProductTabStyleTopTemplateView,
                   SingleProductTemplateView)
from .smartwatch import SmartwatchTemplateView
from .wishlist import WishListView

# from .search import search_products
from shop.views.search import SearchProductsView

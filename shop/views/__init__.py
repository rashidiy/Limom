from .blog_list import (
    BlogPageTemplateView,
    Blog3PageView,
    Blog4PageView,
    Blog5PageView,
    BlogListTemplateView,
    Blog6PageView,
    Blog7PageView,
    Blog8PageView,
    Blog9PageView,
    BlogAudiView,
    BlogVideoView,
    BlogGalaryView
)

from .checkout import CheckOutPageTemplateView

from .compare import CompareTemplateView

from .homepage import HomePageTemplateView

from .login_register import *

from .page_log_reg import (
    ContactView,
    AboutView,
    FaqView,
    ErrorView
)

from .shop import (
    ShopPageTemplateView,
    SingleProductTabStyleLeftTemplateView,
    SingleProductGroupTemplateView,
    SingleProductNormalTemplateView,
    SingleProductTemplateView,
    SingleProductSaleTemplateView,
    SingleProductAffinityTemplateView,
    Shop3PageTemplateView,
    Shop4PageTemplateView,
    ShopRightSidebarPageTemplateView,
    ShopListPageTemplateView,
    ShopListLeftSidebarPageTemplateView,
    ShopListRightSidebarPageTemplateView,
    SingleProductGalleryLeftTemplateView,
    SingleProductCarouselTemplateView,
    SingleProductGalleryRightTemplateView,
    SingleProductTabStyleTopTemplateView,
    SingleProductTabStyleRightTemplateView,
    ShoppingCardTemplateView,
)

from shop.views.about_us import AboutUsTemplateView
from shop.views.contact import ContactTemplateView
from shop.views.accessories import AccessoriesTemplateView
from shop.views.smartwatch import SmartwatchTemplateView
from shop.views.search import SearchProductsView

from .wishlist import WishListView

from .error import custom_404_view

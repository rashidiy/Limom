from .homepage import HomePageTemplateView
from .blog_list import (BlogPageTemplateView ,
                        Blog3PageView ,
                        Blog4PageView ,
                        Blog5PageView ,
                        BlogListTemplateView ,
                        Blog6PageView ,
                        Blog7PageView,
                        Blog8PageView,
                        Blog9PageView,
                        BlogAudiView,
                        BlogVideoView,
                        BlogGalaryView)


from .page_log_reg import (
                           ContactView,
                           AboutView,
                           FaqView,
                           ErrorView)

from .homepage import *
from .checkout import *
from .compare import *
from .shop import *
from .wishlist import *
from .login_register import *

from .shop import (ShopPageTemplateView, SingleProductTabStyleLeftTemplateView, SingleProductGroupTemplateView,
                   SingleProductNormalTemplateView, SingleProductTemplateView, SingleProductSaleTemplateView,
                   SingleProductAffinityTemplateView, Shop3PageTemplateView, Shop4PageTemplateView,
                   ShopRightSidebarPageTemplateView, ShopListPageTemplateView,ShopListPageTemplateView,
                    ShopListLeftSidebarPageTemplateView,ShopListRightSidebarPageTemplateView,
                    SingleProductGalleryLeftTemplateView,SingleProductCarouselTemplateView,SingleProductGalleryRightTemplateView,
                    SingleProductTabStyleTopTemplateView,SingleProductTabStyleRightTemplateView,ShoppingCardTemplateView
                    )
from .wishlist import WishListView
from .checkout import CheckOutPageTemplateView
from .compare import CompareTemplateView

from .error import custom_404_view
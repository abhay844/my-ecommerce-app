
from django.urls import path, re_path
from .views import (
                            ProductListView,
                            # product_list_view,
                            # ProductDetailView,
                            # product_detail_view,
                            # ProductFeaturedListView,
                            # ProductFeaturedDetailView,
                            ProductDetailSlugView
                            )

urlpatterns = [
    re_path(r'^$', ProductListView.as_view()),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # path('products_afv/', product_list_view),
    # re_path(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # re_path(r'products_afv/(?P<pk>\d+)/$', product_detail_view),
    # path("featured/", ProductFeaturedListView.as_view()),
    # re_path(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view())
]
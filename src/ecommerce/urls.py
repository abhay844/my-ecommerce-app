"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from products.views import (
                            ProductListView,
                            product_list_view,
                            ProductDetailView,
                            product_detail_view,
                            ProductFeaturedListView,
                            ProductFeaturedDetailView,
                            ProductDetailSlugView
                            )

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page),
    path('contact/',  views.contact_page),
    path('admin/', admin.site.urls),
    re_path(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('login_page', views.login_page, name='custom_login'),
    path('register', views.register_page, name='register_page'),
    path('products/', ProductListView.as_view()),
    path('products_afv/', product_list_view),
    # re_path(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    re_path(r'products_afv/(?P<pk>\d+)/$', product_detail_view),
    re_path(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    path("featured/", ProductFeaturedListView.as_view()),
    re_path(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view())
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

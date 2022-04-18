# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),             # UI Kits Html files
    # path('products/', include('apps.home.urls')),
    # path('product/', include('apps.product.urls')),
    path('module_products/', include('module_products.urls')),
    path('myapi', include('myapi.urls')),

]

from django.urls import path

from products.views import (
    ProductListCreateView, ProductDetailView
)

urlpatterns = [
    path("", ProductListCreateView.as_view(), name="products_list_create"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="product_detail")
]
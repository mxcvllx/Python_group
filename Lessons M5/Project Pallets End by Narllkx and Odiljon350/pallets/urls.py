from django.urls import path

from pallets.views import HomeView,PalletsListView, PalletsDetailView, AboutUs, Products, Advantages, Contacts

urlpatterns = [
    path('',  HomeView.as_view(), name="homepage"),
    path('pallets/', PalletsListView.as_view(), name="pallets_list"),
    path('pallets/<int:pk>/', PalletsDetailView.as_view(), name="pallets_detail"),
    path('about', AboutUs.as_view(), name='about_us'),
    path('products/', Products.as_view(), name='products'),
    path('advantages/', Advantages.as_view(), name='advantages'),
    path('contacts/', Contacts.as_view(), name='contacts'),
]

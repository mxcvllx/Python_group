from django.urls import path

from common.views import CategoryListCreateView, ContactUsListApiView, AboutUsListApiViews, BlogList, BlogDetail

urlpatterns = [
    path('category/', CategoryListCreateView.as_view(), name='category'),
    path('contact-us/', ContactUsListApiView.as_view(), name='contact-us'),
    path('about-us/', AboutUsListApiViews.as_view(), name='about-us'),
    path('blogs/', BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
]

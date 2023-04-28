from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import Pallets


class HomeView(ListView):
    queryset = Pallets.objects.order_by("-id")
    template_name = "index.html"
    context_object_name = "pallets"


class BaseView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class PalletsListView(ListView):
    queryset = Pallets.objects.order_by("-id")
    template_name = "pallets/pallets.html"
    context_object_name = "pallets"


class PalletsDetailView(DetailView):
    queryset = Pallets.objects.all()
    template_name = "pallets/pallets_detail.html"
    context_object_name = "pallets"


class SearchView(ListView):
    queryset = Pallets.objects.all()
    template_name = "search.html"
    context_object_name = "results"


class AboutUs(ListView):
    queryset = Pallets.objects.all()
    template_name = "products/about_us.html"
    context_object_name = "pallets"


class Products(ListView):
    queryset = Pallets.objects.all()
    template_name = "products/products.html"
    context_object_name = "pallets"


class Advantages(ListView):
    queryset = Pallets.objects.all()
    template_name = "products/advantages.html"
    context_object_name = "pallets"


class Contacts(ListView):
    queryset = Pallets.objects.all()
    template_name = "products/contacts.html"
    context_object_name = "pallets"

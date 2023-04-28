from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from books.models import Book


class HomeView(ListView):
    queryset = Book.objects.order_by("-id")
    template_name = "home.html"
    context_object_name = "books"


class BaseView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class BooksListView(ListView):
    queryset = Book.objects.order_by("-id")
    template_name = "books/books.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = "books/book_detail.html"
    context_object_name = "book"


class SearchView(ListView):
    queryset = Book.objects.all()
    template_name = "search.html"
    context_object_name = "results"


def search(request):
    search_query = request.POST.get("search")
    expression = (
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
    )
    queryset = Book.objects.filter(expression)
    return render(request, "search.html", {"results": queryset})

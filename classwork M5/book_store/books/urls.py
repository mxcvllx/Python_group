from django.urls import path

from books.views import BooksListView, BookDetailView, HomeView, SearchView, search

urlpatterns = [
    path('', HomeView.as_view(), name="homepage"),
    path('books/', BooksListView.as_view(), name="books_list"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('search/', search, name="search")
]
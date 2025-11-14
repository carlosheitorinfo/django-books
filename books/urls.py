# books/urls.py
from django.urls import path
from .views import (BookListView, BookCreateView, BookUpdateView,
                    BookDeleteView, DetailView, publish_book)

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('add/', BookCreateView.as_view(), name='add'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='delete'),
    path('<int:pk>/publish/', publish_book, name='publish'),
]

from django.urls import path, re_path
from books import api


urlpatterns = [
    path("books/", api.BooksListAPI.as_view()),
    re_path(r"^book/(?P<id>\d+)/$", api.BookDetailAPI.as_view()),
    path("add-author/", api.AddAuthorAPI.as_view()),
    path("add-publisher/", api.AddPublisherAPI.as_view()),
    path("add-book/", api.AddBookAPI.as_view()),
    re_path(r"^upd-book/(?P<id>\d+)/$", api.UpdBookAPI.as_view()),
    re_path(r"^del-book/(?P<id>\d+)/$", api.DelBookAPI.as_view())
]

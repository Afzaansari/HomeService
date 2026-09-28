from django.urls import path
from .views import home, book_service


urlpatterns = [
    path("", home, name="home"),
    path("book/", book_service, name="book_service"),
]
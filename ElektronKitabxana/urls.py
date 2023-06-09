from django.urls import path
from . import views

# http://127.0.0.1:8000/ ==> ana sehifeye gedir #1
# http://127.0.0.1:8000/index ==> ana sehifeye gedir #2
# http://127.0.0.1:8000/books ==> books sayfasina

urlpatterns = [
    path('',views.index), 
    path('index',views.index, name="home"),
    path('books',views.books, name="books"),
    path('books/<slug:slug>',views.book_details, name="book_details"),
    path('category/<slug:slug>',views.books_by_category, name="books_by_category"),
    path('author/<slug:slug>',views.books_by_author, name="books_by_author"),
]
    # burada dirnaqin icindeki urldeki localhostdan 
    # sonraki slashdan sonra gelenleri yaziriq
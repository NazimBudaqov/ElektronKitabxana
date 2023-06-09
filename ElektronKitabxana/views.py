from ElektronKitabxana.models import Book, Category, Author
from django.shortcuts import render 

context = {
        "books": Book.objects.all(), 
        #filter(is_active=True, is_home=True) metodu ile her bir funksiyanin
        # icinde(index, books ve s.) filter etmek olar
        "categories": Category.objects.all(),
        "authors": Author.objects.all()
        }

def index(request):
    return render(request, "e-kitab/index.html", context) 

def books(request):
    return render(request, "e-kitab/books.html", context)

def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, "e-kitab/book_details.html", {
        "book":book
    },)

def books_by_category(request, slug):
    context = {
        "books": Book.objects.filter(is_active=True, category__slug=slug), 
        "categories": Category.objects.all(),
        "authors": Author.objects.all(),
        "selected_category": slug

        }
    return render(request, "e-kitab/books.html", context)

def books_by_author(request, slug):
    
    context = {
        "books": Book.objects.filter(is_active=True, author__slug=slug), 
        "categories": Category.objects.all(),
        "authors": Author.objects.all(),
        "selected_author": slug

        }
    return render(request, "e-kitab/books.html", context)



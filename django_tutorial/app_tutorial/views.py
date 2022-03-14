from django.http import HttpResponse
from django.shortcuts import render

from .models import Book, Review


def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('This is about page')

def home(request):
    return HttpResponse('My Home')

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review_detail.html', {'review': review})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})


def book_review_list(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book=book_id)
    return render(request, 'review_list.html', {'reviews': reviews})

from django.http import HttpResponse
from django.shortcuts import render

from .models import Book


def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('This is about page')

def home(request):
    return HttpResponse('My Home')

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})


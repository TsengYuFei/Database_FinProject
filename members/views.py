from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book
from django.views.generic import ListView

def home(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

class BookSearchView(ListView):
    model = Book
    template_name = 'book_search.html'
    context_object_name = 'books'

    def get_queryset(self):
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')
        if query:
            if search_by == 'title':
                return Book.objects.filter(title__icontains=query)
            elif search_by == 'isbn':
                return Book.objects.filter(isbn__icontains=query)
            elif search_by == 'author_last_name':
                return Book.objects.filter(author_lname__icontains=query)
            elif search_by == 'author_first_name':
                return Book.objects.filter(author_fname__icontains=query)
            elif search_by == 'publisher':
                return Book.objects.filter(publisher__icontains=query)
        return Book.objects.none()
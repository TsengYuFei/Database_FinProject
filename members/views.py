from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, BookAuthor
from .forms import BookSearchForm

def home(request):
    form = BookSearchForm()
    return render(request, 'homepage.html', {'form': form})

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
                return Book.objects.filter(bookauthor__ba_lname__icontains=query)
            elif search_by == 'author_first_name':
                return Book.objects.filter(bookauthor__ba_fname__icontains=query)
            elif search_by == 'publisher':
                return Book.objects.filter(publisher__icontains=query)
        return Book.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookSearchForm(self.request.GET)
        return context

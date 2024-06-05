from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Author, Publisher
from .forms import BookSearchForm
from .models import Station

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
            elif search_by == 'lname':
                return Book.objects.filter(author__lname__icontains=query)
            elif search_by == 'fname':
                return Book.objects.filter(author__fname__icontains=query)
            elif search_by == 'publisher':
                return Book.objects.filter(publisher__name__icontains=query)
        return Book.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookSearchForm(self.request.GET)

        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')

        if query:
            if search_by in ['lname', 'fname']:  # 检查是否是搜索作者
                authors = Author.objects.filter(**{'%s__icontains' % search_by: query})
                context['results'] = authors
            elif search_by == 'publisher':  # 检查是否是搜索出版商
                publishers = Publisher.objects.filter(name__icontains=query)
                context['results'] = publishers

        return context

def station_search(request):
    location = request.GET.get('station_location')
    if location:
        stations = Station.objects.filter(addr__icontains=location)
    else:
        stations = Station.objects.none()
    return render(request, 'station_search.html', {'stations': stations})

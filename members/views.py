from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from .models import Administrator, Member, Station, Author, Publisher, Book
from .forms import BookSearchForm

def home(request):
    form = BookSearchForm()
    books = Book.objects.all()
    return render(request, 'homepage.html', {'form': form, 'books': books})

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

def member_info(request):
    if request.method == "POST":
        id = request.POST.get('book_id')
        return_book = Book.objects.get(id=id)
        return_book.statu = "0"
        return_book.save()
        return redirect('member_info')
    member = Member.objects.get(fname="Jack")
    borrowed_books = member.books.all()
    borrowed_books = borrowed_books.filter(statu='1')

    template = loader.get_template('member_info.html')
    context = {
        'member': member,
        'borrowed_books': borrowed_books,
    }
    return HttpResponse(template.render(context, request))

def book_detail(request, id):
    book = Book.objects.get(id = id)
    template = loader.get_template('book_detail.html')
    context = {
        'book': book,
    }
    return HttpResponse(template.render(context, request))

def station_detail(request, id):
    station = Station.objects.get(id = id)
    books = station.books.all().filter(statu='0')
    template = loader.get_template('station_detail.html')
    context = {
        'station': station,
        'books': books,
    }
    return HttpResponse(template.render(context, request))

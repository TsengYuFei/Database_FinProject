from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Administrator, Member, Station, Author, Publisher, Book
from .forms import BookSearchForm

def home(request):
    form = BookSearchForm()
    books = Book.objects.all()
    context = {
        'form': form,
        'books': books,
    }
    return render(request, 'homepage.html', context)

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

@login_required
def member_info(request):
    if request.method == "POST":
        id = request.POST.get('book_id')
        return_book = Book.objects.get(id=id)
        return_book.statu = "0"
        return_book.save()
        return redirect('member_info')
    member = Member.objects.get(user=request.user)
    borrowed_books = member.books.filter(statu='1')

    context = {
        'member': member,
        'borrowed_books': borrowed_books,
    }
    return render(request, 'member_info.html', context)

def book_detail(request, id):
    book = Book.objects.get(id = id)
    context = {
        'book': book,
    }
    return render(request, 'book_detail.html', context)

def station_detail(request, id):
    station = Station.objects.get(id = id)
    books = station.books.filter(statu='0')
    context = {
        'station': station,
        'books': books,
    }
    return render(request, 'station_detail.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
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
        queryset = Book.objects.all()

        title_query = self.request.GET.get('title_query')
        isbn_query = self.request.GET.get('isbn_query')
        lname_query = self.request.GET.get('lname_query')
        fname_query = self.request.GET.get('fname_query')
        publisher_query = self.request.GET.get('publisher_query')

        if title_query and 'search_by_title' in self.request.GET:
            queryset = queryset.filter(title__icontains=title_query)
        if isbn_query and 'search_by_isbn' in self.request.GET:
            queryset = queryset.filter(isbn__icontains=isbn_query)
        if lname_query and 'search_by_lname' in self.request.GET:
            queryset = queryset.filter(author__lname__icontains=lname_query)
        if fname_query and 'search_by_fname' in self.request.GET:
            queryset = queryset.filter(author__fname__icontains=fname_query)
        if publisher_query and 'search_by_publisher' in self.request.GET:
            publisher_query = publisher_query.strip()  # 移除空格
            queryset = queryset.filter(publisher__name__iexact=publisher_query) # 返回與輸入的出版社名稱完全匹配的書籍
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
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
    borrow_success = False
    if request.method == "POST":
        member = Member.objects.get(user=request.user)
        id = request.POST.get('book_id')
        return_book = Book.objects.get(id=id)
        return_book.statu = "1"
        return_book.member = member
        return_book.save()
        borrow_success = True
        context = {
            'book': book,
            'borrow_success': borrow_success,
        }
        return render(request, 'book_detail.html', context)
    book = Book.objects.get(id = id)
    context = {
        'book': book,
        'borrow_success': borrow_success,
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

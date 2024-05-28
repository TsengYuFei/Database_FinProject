from django.urls import path
from . import views
from .views import BookSearchView

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', BookSearchView.as_view(), name='book_search'),
]
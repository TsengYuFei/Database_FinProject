from django.urls import path
from . import views
from .views import BookSearchView

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', BookSearchView.as_view(), name='book_search'),
    path('station_search/', views.station_search, name='station_search'),
    path('member/', views.member_info, name='member_info'),
]
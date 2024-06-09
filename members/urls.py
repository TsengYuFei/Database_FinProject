from django.urls import path
from . import views
from .views import BookSearchView
from .views import MemberSearchView

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', BookSearchView.as_view(), name='book_search'),
    path('member_search/', MemberSearchView.as_view(), name='member_search'),
    path('station_search/', views.station_search, name='station_search'),
    path('member/', views.member_info, name='member_info'),
    path('book/<int:id>', views.book_detail, name='book_detail'),
    path('station/<int:id>', views.station_detail, name='station_detail'),
    path('login/', views.login, name='login'),
    path('login_successful/', views.login_successful, name='login_successful'),
    path('register/', views.register, name='register'),
    path('register_successful/', views.register_successful, name='register_successful'),
    path('logout/', views.logout, name='logout'),
    path('sulogout/', views.superuser_logout, name='superuser_logout'),
    
]
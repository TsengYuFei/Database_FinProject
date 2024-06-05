from django.contrib import admin
from .models import Administrator, Member, Station, Author, Publisher, Book

# Register your models here.

class AdministratorAdmin(admin.ModelAdmin):
    list_display = ("fname", "lname")
admin.site.register(Administrator, AdministratorAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ("fname", "lname", "phone", "ssn", "sex")
admin.site.register(Member, MemberAdmin)

class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "statu", "addr")
admin.site.register(Station, StationAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("fname", "lname")
admin.site.register(Author, AuthorAdmin)

# class PublisherAdmin(admin.ModelAdmin):
#     list_display = ("name")
# admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Publisher)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn", "statu")
admin.site.register(Book, BookAdmin)

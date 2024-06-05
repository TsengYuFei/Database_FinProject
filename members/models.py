from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=25, verbose_name='書名')
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN')
    author_lname = models.CharField(max_length=5, verbose_name='姓')
    author_fname = models.CharField(max_length=20, verbose_name='名')
    publisher = models.CharField(max_length=20, verbose_name='出版社')

    def __str__(self):
        return self.title

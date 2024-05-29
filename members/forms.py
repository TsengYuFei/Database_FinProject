from django import forms

class BookSearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('title', '書名'),
        ('isbn', 'ISBN'),
        ('author_last_name', '姓'),
        ('author_first_name', '名'),
        ('publisher', '出版社'),
    ]
    search_by = forms.ChoiceField(choices=SEARCH_CHOICES, label='搜尋類別')
    query = forms.CharField(max_length=25, required=False)
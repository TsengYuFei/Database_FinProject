from django import forms

class BookSearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('title', '書名'),
        ('isbn', 'ISBN'),
        ('lname', '姓'),
        ('fname', '名'),
        ('publisher', '出版社'),
    ]
    search_by = forms.MultipleChoiceField(choices=SEARCH_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)
    query = forms.CharField(max_length=25, required=False)

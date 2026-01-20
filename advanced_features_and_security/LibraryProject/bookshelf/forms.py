from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class BookSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)
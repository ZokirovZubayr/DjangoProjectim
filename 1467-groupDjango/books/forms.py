from django import forms

from .models import Book, Car, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

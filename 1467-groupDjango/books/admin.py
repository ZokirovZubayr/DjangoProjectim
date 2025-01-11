from django.contrib import admin
from .models import Book, Author, Choice


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    search_fields = ["title"]
    list_filter = ['id', 'title', 'price']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'bio']
    search_fields = ["email"]
    list_filter = ['id', 'first_name', 'last_name']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['colors']
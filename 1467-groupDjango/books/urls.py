from django.urls import path
from .views import authors_page, data_page, cars_view, books_view, manu, delete_book_view, edit_book_view, \
    edit_car_view, delete_car_view, edit_author_view, delete_author_view

urlpatterns = [
    path('data_page/', data_page, name='data_page'),
    path('cars_view/', cars_view, name='cars_view'),
    path('books_view/', books_view, name='books_view'),
    path('authors_page/', authors_page, name='authors_page'),
    path('manu/', manu, name='manu'),
    path('edit_book_view/<int:pk>/', edit_book_view, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book_view, name='delete_book'),
    path('edit_car_view/<int:pk>/', edit_car_view, name='edit_car'),
    path('delete_car_view/<int:pk>/', delete_car_view, name="delete_car"),
    path('edit_author/<int:pk>/', edit_author_view, name='edit_author'),  # ✅ Corrected syntax <int:pk>.
    path('delete_author/<int:pk>/', delete_author_view, name='delete_author'),  # ✅ Corrected syntax <int:pk>.
]


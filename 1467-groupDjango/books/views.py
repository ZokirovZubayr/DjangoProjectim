from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Car, Book
from .forms import BookForm, CarForm, AuthorForm


# Create your views here.
def authors_page(request):
    authors = Author.objects.all()
    data = {
        'authors': authors
    }
    return render(request, "author.html", data)


def data_page(request):
    data = Author.objects.all()
    context = {"data": data}
    return render(request, 'data.html', context)


def cars_view(request):
    cars = Car.objects.all()
    data = {
        'cars': cars
    }
    return render(request, 'cars.html', data)


def books_view(request):
    books = Book.objects.all()
    data = {
        "books": books
    }
    return render(request, 'books.html', data)


def manu(request):
    return render(request, 'manu.html')


def edit_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_view')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form})


def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('books_view')


def edit_car_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars_view')
    else:
        form = CarForm(instance=car)
    return render(request, 'edit_car.html', {'form': form})


def delete_car_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('cars_view')


# Authors

def edit_author_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)  # ✅ Corrected request.POST
        if form.is_valid():
            form.save()
            return redirect('authors_page')
    else:
        form = AuthorForm(instance=author)  # ✅ Moved this block to handle non-POST requests.
    return render(request, 'edit_author.html', {'form': form})  # ✅ Corrected dictionary syntax.


def delete_author_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return redirect('authors_page')

from django.shortcuts import render, get_object_or_404,redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


# imports from your created files
from books.models import book
from books.forms import BookModelForm

books = [
    {"id": 1, "title": "Rust", "no_pages": 300, "author": "author", "price": 100, "image": "1.jpg"},
    {"id": 2, "title": "C", "no_pages": 350, "author": "author", "price": 150, "image": "2.jpg"},
    {"id": 3, "title": "python", "no_pages": 450, "author": "author", "price": 250, "image": "3.jpg"},
    {"id": 4, "title": "Rust", "no_pages": 300, "author": "author", "price": 100, "image": "1.jpg"},
    {"id": 5, "title": "C", "no_pages": 350, "author": "author", "price": 150, "image": "2.jpg"},
    {"id": 6, "title": "Python", "no_pages": 300, "author": "author", "price": 250, "image": "3.jpg"},
]


def book_details(request, id):
    filtered_books = filter(lambda book: book['id'] == id, books)
    filtered_books = list(filtered_books)
    if filtered_books:
        book = filtered_books[0]
        return render(request, "books/details.html", context={"book":book})


def books_home(request):
    return render(request, "books/home.html", context={"books": books}, status=200)


def contact_us(request):
    return render(request, "books/contactus.html", status=200)


def about_us(request):
    return render(request, "books/aboutus.html", status=200)


def books_index(request):
    books  = book.objects.all()
    return render(request, "books/homedatabase.html",
                  context={"books": books})


@login_required
def book_show(request, id):
    bookdata = get_object_or_404(book, pk=id)
    return render(request, "books/detailsdatabase.html", context={"bookdata": bookdata})


@login_required
def book_delete(request, id):
    bookdata = get_object_or_404(book, pk=id)
    bookdata.delete()
    url = reverse("homedatabase")
    return redirect(url)


def book_create(request):
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        newbook = book(title=request.POST["title"], price=request.POST["price"], author=request.POST["author"],
                          no_pages=request.POST["no_pages"], image=image)
        newbook.save()
        url = reverse("homedatabase")
        return redirect(url)
    return  render(request, 'books/create.html')


def book_update(request,id):
    bookdata = get_object_or_404(book, pk=id)
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = bookdata.image
        bookdata.title = request.POST["title"]
        bookdata.author = request.POST["author"]
        bookdata.price = request.POST["price"]
        bookdata.no_pages = request.POST["no_pages"]
        bookdata.image = image
        bookdata.save()
        url = reverse("homedatabase")
        return redirect(url)

    return render(request, "books/update.html", {"bookdata":bookdata})


@login_required
def book_create_forms(request):
    form = BookModelForm()
    if request.method == "POST":
        if request.FILES:
            image = request.FILES["image"]
        else:
            image = None
        form = BookModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            url = reverse("homedatabase")
            return redirect(url)

    return render(request, 'books/forms/create.html', context={'form': form})


@login_required
def book_edit_forms(request, id):
    bookdata=get_object_or_404(book, pk=id)
    form = BookModelForm(instance=bookdata)
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES, instance=bookdata)
        if form.is_valid():
            form.save()
            url = reverse("homedatabase")
            return redirect(url)

    return render(request, 'books/forms/update.html',
              context={"form": form})



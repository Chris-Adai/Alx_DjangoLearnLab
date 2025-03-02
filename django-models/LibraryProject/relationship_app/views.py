from django.shortcuts import render, redirect
# from django.shortcuts import render
# from django.views.generic import DetailView
from django.views.generic.detail import DetailView
# from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Library
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from django.contrib.auth.decorators import permission_required

# Create your views here.
# from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    # template_name = "library_detail.html"
    context_object_name = "library"


# from django.contrib.auth import login, logout
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.shortcuts import render, redirect

# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("list_books")
#     else:
#         form = UserCreationForm()
#     return render(request, "relationship_app/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


# from django.views.generic.detail import DetailView
# from django.shortcuts import render
# from .models import Library  # Ensure Library model exists

# # Class-Based View for displaying library details
# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = "relationship_app/library_detail.html"
#     context_object_name = "library"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})



@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        if title and author and published_date:
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('book_list')

    return render(request, 'add_book.html')

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book_list')

    return render(request, 'edit_book.html', {'book': book})

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'confirm_delete.html', {'book': book})





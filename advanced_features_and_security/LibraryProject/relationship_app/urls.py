from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView
from .views import register_view, login_view, logout_view
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view
# from .views import admin_view
# from .views import librarian_view
# from .views import member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    # path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # path('books/add/', add_book, name='add_book'),
    # path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('add_book/', add_book, name='add_book'),  # ✅ Matches the expected pattern
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),  # ✅ Matches the expected pattern
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),

    
]

urlpatterns += [
    # path("register/", register_view, name="register"),
    path("register/", views.register, name="register"),  # ✅ Use `views.register`
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", register, name="register"),
]


#######################################################


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

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    # path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
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


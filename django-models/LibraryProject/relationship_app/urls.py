from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView
from .views import register_view, login_view, logout_view

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    # path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
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

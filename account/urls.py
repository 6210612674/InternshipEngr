from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [path("", views.index, name="index"),
               path("register", views.register, name="register"),
               path("login", views.login, name="login"),
               path("logout", views.logout, name="logout"),
               path("register_page", views.register_page, name="register_page"),
               path("login_page", views.login_page, name="login_page"),
               path("profile", views.profile, name="profile"),
               ]

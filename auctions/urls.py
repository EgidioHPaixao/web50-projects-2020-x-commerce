from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("auction/new", views.newListing, name="newListing"),
    path("auction/active", views.activeListings, name="activeListings"),
    path("auction/watchlist", views.watchlist, name="watchlist")
]

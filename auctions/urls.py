from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("auction/new", views.newListing, name="newListing"),    
    path("auction/active", views.activeListings, name="activeListings"),
    path("auction/active/<int:category_id>", views.activeListings, name="activeListings"),
    path("auction/watchlist", views.watchlist, name="watchlist"),
    path("auction/watchlist/<int:listing_id>/change/<str:reverse_method>", views.change_watchlist, name="change_watchlist"),
    path("auction/listing/<int:listing_id>", views.listing, name="listing"),
    path("auction/listing/<int:listing_id>/bid", views.take_bid, name="take_bid"),    
    path("auction/listing/<int:listing_id>/close", views.close_listing, name="close_listing"),
    path("auction/listing/<int:listing_id>/comment", views.comment, name="comment"),
]

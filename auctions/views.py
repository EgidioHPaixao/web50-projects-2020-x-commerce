from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.forms import ModelForm,  modelformset_factory
from .models import Listing, User, Picture

from django.contrib.auth.decorators import login_required

class newListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'startingBid', 'category']

class newPictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['picture']

def index(request):
    return render(request, "auctions/index.html")

@login_required
def newListing(request):
    PictureFormSet = modelformset_factory(Picture,
                                        form=newPictureForm, extra=3)
    if request.method == "POST":        
        form = newListingForm(request.POST)
        if form.is_valid():
            print(f"ta certo")
            newListing = form.save(commit=False)
            newListing.creator = request.user
            newListing.save()
            return render(request, "auctions/newListing.html", {
                "form": newListingForm(),
                "formset": formset,
                "success": True
        })
        else:
            print(f"ta errado")
        
    else:
        return render(request, "auctions/newListing.html", {
            "form": newListingForm(),
            "imageForm": PictureFormSet(queryset=Picture.objects.none())
        })

def activeListings(request):
    listings = Listing.objects.all()
    return render(request, "auctions/active.html", {
        "listings": listings
    })
    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

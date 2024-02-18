# views.py

from django.shortcuts import render, redirect
from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import MenuItem, Reservation, Review, Special
#from .models import Special
from .forms import ReviewForm
from django.http import HttpResponse
from .models import GalleryImage

def home(request):
    return render(request, 'home.html')

def menu(request):
    menu_items = MenuItem.objects.all()
    print(menu_items)
    return render(request, 'menu.html', {'menu_items': menu_items})

def contact(request):
    if request.method == 'POST':
        # Process form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Here you can perform actions like sending an email or saving the message to the database
        return HttpResponse('Thank you for your message!')
    else:
        return render(request, 'contact.html')
def about(request):
    # Provide about us content
    return render(request, 'about.html')

def gallery(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'gallery/gallery.html', {'gallery_images': gallery_images})

def specials(request):
    # Fetch and display specials/promotions
    specials = Special.objects.all()
    return render(request, 'specials.html', {'specials': specials})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth import logout
from .models import University
from .models import Review
from .forms import ReviewForm
from .models import UniversityTestimonial





# Create your views here.
def leaderboard(request):
   myunis = University.objects.all().order_by('-overallScore').values()
   #template = loader.get_template('unis.html')
   return render(request, "unis.html", {"myunis":myunis})

def university_detail(request, university_id):
    university = get_object_or_404(University, pk=university_id)

   
    star_count = university.get_labeling_star_rating()  
    empty_stars=5-star_count
    progress_bar_pct=university.get_overall_score()/740*100

    images = university.images.all()
    approved_reviews = university.review_set.filter(approved=True).order_by('-created_at')

    approved_testimonials=university.testimonials.filter(approved=True)




    
    #this render function allows unidetails.html to access all of these variables that we defined in this view.
    return render(request, 'unidetails.html', {
        'university': university,
        'star_count': star_count,
        'filled_stars':range(star_count),
        'empty_stars': range(empty_stars),
        'progress_bar_pct': progress_bar_pct,
        'images': images,
        'reviews': approved_reviews,
        'testimonials': approved_testimonials
          })


def home(request):
    myunis = University.objects.all().values()
    return render(request, "home.html", {"myunis":myunis})

def about(request):
    return render(request, "about.html")

def login_view(request):
    return render(request, "login.html")


def logout_view(request):
    """Handle user logout"""
    logout(request)
    return redirect('login')

def methodology_view(request):
    return render(request, "methodology.html")

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    already_submitted = Review.objects.filter(user=request.user).exists()
    
    if request.method == 'POST' and not already_submitted:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('profile')  # Replace with your success URL
    else:
        form = ReviewForm() if not already_submitted else None
    
    user_reviews = Review.objects.filter(user=request.user).order_by('-created_at')

    
    return render(request, 'profile.html', {
        'form': form,
        'already_submitted': already_submitted,
        'user_reviews': user_reviews
    })
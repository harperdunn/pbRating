from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .models import University
from pathlib import Path
from .forms import TestimonialForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests




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
#This is all commented out below because instead we now do all path handling within the model and image upload so that the captions are associated and it is smoother.

     # Path to the folder containing the university's images
    # carousel_folder = Path('media') / university.image_folder #calls the property method
    #instead of the above we can just do university.image_folder property
    # image_folder=university.image_folder
    # #list of all image files in the folder
    # image_files = [f for f in image_folder.iterdir() if f.is_file() and f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif']]
    
    # # Extract the relative paths for use in templates
    # image_urls = [f"/media/{university.image_folder}/{f.name}" for f in image_files]

     # Fetch UniversityImage objects associated with the university
    images = university.images.all()

    # Create a list of dictionaries containing image URLs and captions
   

    #fetch testimonials linked to the uni
    testimonials = university.testimonials.all()

    # Get approved testimonials only
    testimonials = university.testimonials.filter(approved=True)
    
    # Handle testimonial submission
    if request.method == 'POST' and 'submit_testimonial' in request.POST:
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.university = university
            if request.user.is_authenticated:
                testimonial.user = request.user
                testimonial.name = request.user.get_full_name() or request.user.username
            testimonial.save()
            messages.success(request, 'Thank you for your testimonial! It will be reviewed before appearing.')
            return redirect('university_detail', university_id=university.id)
    else:
        form = TestimonialForm()
    
    #this render function allows unidetails.html to access all of these variables that we defined in this view.
    return render(request, 'unidetails.html', {
        'university': university,
        'star_count': star_count,
        'filled_stars':range(star_count),
        'empty_stars': range(empty_stars),
        'progress_bar_pct': progress_bar_pct,
        'images': images,
        'testimonials': testimonials,
        'testimonial_form': form,
          })


def home(request):
    myunis = University.objects.all().values()
    return render(request, "home.html", {"myunis":myunis})

def about(request):
    return render(request, "about.html")

def signin(request):
    return render(request, "signin.html")

@csrf_exempt
def sign_in(request):
    return render(request, 'sign_in.html')

@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    print('Inside')
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
        )
    except ValueError:
        return HttpResponse(status=403)

    # In a real app, I'd also save any new user here to the database.
    # You could also authenticate the user here using the details from Google (https://docs.djangoproject.com/en/4.2/topics/auth/default/#how-to-log-a-user-in)
    request.session['user_data'] = user_data

    return redirect('sign_in')

def sign_out(request):
    del request.session['user_data']
    return redirect('sign_in')

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import University
from pathlib import Path

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
    
    #this render function allows unidetails.html to access all of these variables that we defined in this view.
    return render(request, 'unidetails.html', {
        'university': university,
        'star_count': star_count,
        'filled_stars':range(star_count),
        'empty_stars': range(empty_stars),
        'progress_bar_pct': progress_bar_pct,
        'images': images,
        'testimonials': testimonials,
          })


def home(request):
    myunis = University.objects.all().values()
    return render(request, "home.html", {"myunis":myunis})

def about(request):
    return render(request, "about.html")

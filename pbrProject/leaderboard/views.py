from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import University

# Create your views here.
def leaderboard(request):
   myunis = University.objects.all().order_by('-overallScore').values()
   #template = loader.get_template('unis.html')
   return render(request, "unis.html", {"myunis":myunis})

def university_detail(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    return render(request, 'unidetails.html', {'university': university})


def home(request):
    myunis = University.objects.all().values()
    return render(request, "home.html", {"myunis":myunis})

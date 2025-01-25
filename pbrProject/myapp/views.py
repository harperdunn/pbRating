from django.shortcuts import render, HttpResponse #can render html templates or import http response

# Create your views here.
def home(request):
    return HttpResponse("hello world!")
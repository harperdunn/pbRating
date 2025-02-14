from django.shortcuts import render, HttpResponse #can render html templates or import http response
from .models import TodoItem #access all instances of TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all() #gets all objects that exist inside database field
    return render(request, "todos.html", {"todos": items})
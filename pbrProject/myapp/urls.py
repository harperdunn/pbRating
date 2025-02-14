from django.urls import path
from . import views

urlpatterns= [
    path("",views.home, name="home"),#empty path, base url
    path("todos/", views.todos, name="Todos"),
]
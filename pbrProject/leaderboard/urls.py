from django.urls import path
from . import views

urlpatterns = [
    path('', views.leaderboard, name='leaderboard'),
    path('universities/<int:university_id>/', views.university_detail, name='university_detail')
]
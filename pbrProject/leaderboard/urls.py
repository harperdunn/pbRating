from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.leaderboard, name='leaderboard'),
    path('universities/<int:university_id>/', views.university_detail, name='university_detail'),
    path('about/', views.about, name="about" )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
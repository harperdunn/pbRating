from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.leaderboard, name='leaderboard'),
    path('universities/<int:university_id>/', views.university_detail, name='university_detail'),
    path('about/', views.about, name="about" ),
    # path('signin/', views.signin, name="signin"), commenting out bc allauth handles this view
    path('accounts/', include('allauth.urls')),  # Handles ALL Google auth (login/signup)
    # path('accounts/', include('allauth.socialaccount.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
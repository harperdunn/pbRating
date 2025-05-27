from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.leaderboard, name='leaderboard'),
    path('universities/<int:university_id>/', views.university_detail, name='university_detail'),
    path('about/', views.about, name="about" ),
    path('login/', views.login_view, name="login"), 
    path("logout/",views.logout_view, name="logout" ),
    path('profile/', views.profile_view, name='profile'),
    path('methodology/', views.methodology_view, name='methodology'),
    path('delete-review/', views.delete_review, name='delete_review'),
    path('accounts/', include('allauth.urls')),  # Handles ALL Google auth (login/signup), jumps to the allauths accounts folder of templates etc
    # path('accounts/', include('allauth.socialaccount.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
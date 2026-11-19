from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('programmes/apply/', views.programme_application, name='programme_application'),
    path('events/', views.events, name='events'),
    path('blog/', views.blog, name='blog'),
    path('gallery/', views.gallery, name='gallery'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path('membership/', views.membership, name='membership'),
]

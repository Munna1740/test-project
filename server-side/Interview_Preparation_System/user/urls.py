from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/',views.login, name='login'),
    path('registration/',views.registration, name='registration'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),

    path('', views.landingPage, name='landingPage'),
    path('landingpage/', views.landingPage, name='landingpage'),
    path('home/', views.home, name='home'),
    path('upload_resume/', views.upload_resume, name='fileupload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
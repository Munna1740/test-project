from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', views.landingPage, name='landingPage'),
    path('home/', views.home, name='home'),
    path('upload_resume/', views.upload_resume, name='fileupload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
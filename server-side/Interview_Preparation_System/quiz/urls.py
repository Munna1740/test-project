from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('quiz/', views.welcome, name='welcome'),
    path('evaluate/', views.evaluate, name='evaluate'),

]

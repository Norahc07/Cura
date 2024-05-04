from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('symptoms-checker/', views.symptomschecker, name='symptoms-checker'),
    path('consultation-booking/', views.consultationbooking, name='consultation-booking'),
    path('history/', views.history, name='history'),
    path('doctor/', views.doctor, name='doctor'),
]

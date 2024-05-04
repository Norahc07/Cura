from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def home(request):
    return render(request, 'myapp/home.html')

def symptomschecker(request):
    return render(request, 'myapp/symptoms.html')

def consultationbooking(request):
    return render(request, 'myapp/consult.html')

def history(request):
    return render(request, 'myapp/history.html')

def doctor(request):
    return render(request, 'myapp/doctor.html')

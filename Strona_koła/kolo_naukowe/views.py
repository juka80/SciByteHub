from django.shortcuts import render

def home(request):
    return render(request, 'kolo_naukowe/home.html')
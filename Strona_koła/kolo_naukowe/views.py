from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request, 'kolo_naukowe/home.html')

class ContactView(TemplateView):
    template_name = "kontakt.html"

class CoursesView(TemplateView):
    template_name = "kursy.html"

class AboutView(TemplateView):
    template_name = "onas.html"

from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class ContactView(TemplateView):
    template_name = "kontakt.html"

class CoursesView(TemplateView):
    template_name = "kursy.html"

class AboutView(TemplateView):
    template_name = "onas.html"

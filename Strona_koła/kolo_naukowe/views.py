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

class MembersView(TemplateView):
    template_name = "czlonkowie.html"

from django.http import FileResponse
import os
from django.conf import settings

def download_pdf(request):
    filepath = os.path.join(settings.MEDIA_ROOT, 'Plan-kursu-Python-2024.pdf')
    pdf = open(filepath, 'rb')
    response = FileResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'Plan-kursu-Python-2024.pdf'
    return response

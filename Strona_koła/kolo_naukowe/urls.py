from django.urls import path
from .views import ContactView, CoursesView, AboutView, HomeView
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path("kontakt/", ContactView.as_view(), name="kontakt"),
    path("kursy/", CoursesView.as_view(), name="kursy"),
    path("onas/", AboutView.as_view(), name="onas"),
    #path('about/', views.about, name='about'),  
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from django.http import HttpResponse
from . import views

app_name = 'logistics'

#def home_view(request):
#    return HttpResponse("Home Page")

urlpatterns = [
    # Home page
    #path('', home_view, name='home'),
    path('', views.home, name='home'),
    # About page
    path('about/', views.about, name='about'),
    # Contact page
    path('contact/', views.contact, name='contact'),
]
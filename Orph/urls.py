from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('suggestion', views.suggestion, name='suggestion'),
    path('donation', views.donation, name='donation')
]

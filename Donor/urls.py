from . import views
from django.urls import path

urlpatterns = [
    path('', views.donor, name='donor'),
    path('add_profile', views.add_profile, name='add_profile'),
    path('view_donation', views.view_donation, name='view_donation'),
    path('visit', views.visit, name='visit')
]

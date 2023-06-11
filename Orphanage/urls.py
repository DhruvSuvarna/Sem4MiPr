from . import views
from django.urls import path

urlpatterns = [
    path('', views.orphanage, name='orphanage'),
    path('view_donations', views.view_donations, name='view_donations'),
    path('add_details', views.add_details, name='add_details'),
    path('view_details', views.view_details, name='view_details'),
    path('add_events', views.add_events, name='add_events'),
    path('check_visits', views.check_visits, name='check_visits')
]
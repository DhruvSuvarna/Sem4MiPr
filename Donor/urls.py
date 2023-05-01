from . import views
from django.urls import path

urlpatterns = [
    path('', views.donor, name='donor'),
    path('thankyou', views.thankyou, name='thankyou')
]

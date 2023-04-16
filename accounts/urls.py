from django.urls import path
from . import views

urlpatterns = [
    path('authform', views.authform, name='authform'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('o_signup', views.o_signup, name='o_signup'),
    path('o_signin', views.o_signin, name='o_signin'),
    path('o_signout', views.o_signout, name='o_signout'),
]
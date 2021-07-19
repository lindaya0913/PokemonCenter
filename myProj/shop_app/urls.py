from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.app_homepage, name='app_homepage'),
    path('about_us', views.about_us, name='about_us'),
    path('services', views.services, name='services'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('loggedin', views.loggedin, name='loggedin'),
    path('logout', views.logout, name='logout'),
]
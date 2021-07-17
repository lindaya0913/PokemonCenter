from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.homepage),
    path('', include('shop_app.urls'))
]

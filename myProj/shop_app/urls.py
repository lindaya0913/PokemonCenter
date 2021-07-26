from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from products_app import views as prod_views

urlpatterns = [
    path('', views.app_homepage, name='app_homepage'),
    path('about_us', views.about_us, name='about_us'),
    path('services', views.services, name='services'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('loggedin', views.loggedin, name='loggedin'),
    path('logout', views.logout, name='logout'),
    path('userlist', views.UserListView.as_view(), name='userlist'),
    path('userdetail/<int:pk>', views.UserDetailView.as_view(template_name='user_detail.html'), 
        name='userdetail'),
    path('usercreate/', views.UserCreateView.as_view(template_name='user_create.html'), 
        name='usercreate'),  
    path('userupdate/<int:pk>', views.UserUpdateView.as_view(template_name='user_create.html'), 
        name='userupdate'),
    path('userdelete/<int:pk>', views.UserDeleteView.as_view(template_name='user_delete.html'), 
        name='userdelete'),
    path('products', prod_views.product_list, name='products_list'),
    path('order', prod_views.order, name='order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
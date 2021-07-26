from django.shortcuts import render, redirect
from .models import OrderList
from django.contrib import messages
from shop_app import views as shop_view
from shop_app import models as shop_model
from django.core.mail import send_mail
from django.conf import settings

def product_list(request):
    products = {'closing': ['Pikachu','Ditto'],
                'figures': ['Pikachu Relaxing River Figure','Charmander Relaxing River Figure','Nendoroid Green Posable Figure'],
                'plush': ['Kanto','Johto','Hoenn'],
                'cards': ['Card Sleeves','Deck Boxes'],
                'home_stuff': ['Socks','T-Shirts','Shirts','Jackets'],
                'video_game_stuff': ['Books','Water Bottle','Poster']}
    return render(request, 'products_list.html', products)

def order(request):
    if request.method == 'POST':
        prod_list = request.POST.getlist('products')
        prod_str = ','.join(prod_list)
        order_data = OrderList(wholelist=prod_str, username=shop_view.username)
        order_data.save()
        user_data = shop_model.RegisteredUser.objects.get(name=shop_view.username)
        recipientlist = [user_data.email,]
        send_mail(
            'Order from Pokémon Center',
            'Hi, \n \n Below are the products that you have orderd from Pokémon Center. \n \n {}'.format(prod_str),
            settings.EMAIL_HOST_USER,
            recipientlist
        )
        messages.success(request, 'Order has been created successfully and a mail with the list of products has been sent to your registered email address')
        return render(request, 'ordersuccess.html')
    else:
        return render(request, 'product_list.html')
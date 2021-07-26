from django.shortcuts import render, redirect
from .models import OrderList
from django.contrib import messages
from shop_app import views as shop

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
        order_data = OrderList(wholelist=prod_str, username=shop.username)
        order_data.save()
        messages.success(request, 'Order created successfully:' + prod_str)
        return redirect('loggedin')
    else:
        return render(request, 'product_list.html')
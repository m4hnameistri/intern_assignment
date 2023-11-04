from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import JsonResponse
from .cart import Cart
# Create your views here.
def index(request):
    products = Product.objects.all()
    cart = Cart(request)

    return render(request, 'base.html', {'products': products, 'cart': cart})

def add_to_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id = product_id)
        check = cart.add(product=product)
        print(check)
        for k in request.session['cart'].items():
            print(k)
        cart_qty = cart.__len__()
        total_cart = cart.total_cart_price()
        response = JsonResponse({'id': product_id, 'soluong': product_qty, 'cart_qty': cart_qty, 'total_cart': total_cart, 'check': check})
        # for key, value in request.session.items():
        #     print('{} =++=> {}'.format(key, value))

        return response 

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))

        cart.delete(product = product_id)

        cart_qty = cart.__len__()
        total_cart = cart.total_cart_price()
        response = JsonResponse({'cartqty': cart_qty, 'total_cart': total_cart})
        # return render(request, 'cart/summary.html', response)
    return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        print(product_qty)
        if product_qty == 0:
            cart.delete(product=product_id)
        cart.update(product = product_id, product_qty = product_qty)

        cart_qty = cart.__len__()
        cart_total = cart.total_cart_price()
        print(cart_total)
        # item_total = cart.total_item_price(str(product_id))
        response = JsonResponse({'cartqty': cart_qty, 'cart_total': cart_total})
        # return render(request, 'cart/summary.html', response) 
        return response



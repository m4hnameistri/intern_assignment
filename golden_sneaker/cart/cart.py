from decimal import Decimal
from .models import Product


class Cart():
    # A base Cart class, providing some default behaviors that can be inherited or
    #  overrided, as necessary
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if 'cart' not in request.session:
            cart = self.session['cart'] = {}
        self.cart = cart 

    def add(self, product):
        check = 1
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'soluong': 1}
            self.save()

        else:
            check = 0
        return check

    def delete(self, product):
        # Delete item from session data
        product_id = str(product)
        
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def update(self, product, product_qty):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['soluong'] = product_qty
        self.save()        
    
    def __iter__(self):
        ### Colect the product_id from the session data to query the database and return products we need
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['soluong']
            yield item 

    def __len__(self):
        ### Get the cart data and count the quantity of items
        return sum(item['soluong'] for item in self.cart.values())
    
    def total_cart_price(self):
        cart = self.cart.copy()
        return sum(Decimal(item['price']) * item['soluong'] for item in cart.values())
    
    def save(self):
        self.session.modified = True



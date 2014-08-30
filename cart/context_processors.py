from cart import Cart

def get_cart(request):
    return {'get_cart':Cart(request)}
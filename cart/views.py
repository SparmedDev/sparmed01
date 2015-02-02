from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from cart import Cart
from shop.models import Product, Category
from online_order.models import InventoryAddToCartForm

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_pk = request.POST.get("product_pk")              
        quantity = request.POST.get("quantity", 1) 
        
        product = get_object_or_404(Product, pk=product_pk)
        cart = Cart(request)
        cart.add(product, quantity)
    
        return HttpResponse('success')
    
    return HttpResponse('error')

@login_required
def remove_from_cart(request, object_id):
    product = Product.objects.get(id=object_id)
    cart = Cart(request)
    try:
        cart.remove(product)
    except Item.DoesNotExist:
        pass
    
    return HttpResponseRedirect(reverse('online_order.views.order_online'))

@login_required
def set_quantity_on_product(request):
    if request.method == 'POST':
        for key, value in request.POST.iteritems():
            if value.isdigit():
                object_id = key.split('_')[0]
                if object_id.isdigit():
                    product = Product.objects.get(id=object_id)
                    cart = Cart(request)
                    cart.set_product_quantity(product, value)

    return HttpResponseRedirect(reverse('online_order.views.order_online'))
  
@login_required  
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
  
    return HttpResponseRedirect(reverse('online_order.views.order_online'))
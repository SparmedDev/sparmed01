from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from cart import Cart
from shop.models import Product, Category
from online_order.models import InventoryAddToCartForm

@login_required
def add_to_cart(request, category_slug, object_id, quantity=1):
    product = Product.objects.get(id=object_id)
    cart = Cart(request)
    cart.add(product, quantity)    
        
    return HttpResponseRedirect(reverse('shop.views.products'))
  
@login_required
def add_to_cart_inventory(request):
    if request.method == 'POST':
        form = InventoryAddToCartForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            
            product = Product.objects.get(id=product_id)
            cart = Cart(request)
            cart.add(product, quantity)
        
    return HttpResponseRedirect(reverse('sparmed.views.inventory'))     

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
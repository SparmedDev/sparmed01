from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from cart import Cart
from shop.models import Product, Category


@login_required
def add_to_cart(request, category_slug, object_id,quantity=1):
    product = Product.objects.get(id=object_id)
    if product:
        cart = Cart(request)
        cart.add(product, quantity)    

    category = Category.objects.get(slug=category_slug)  
    categories = Category.objects.all()    
    
    return HttpResponseRedirect(reverse('shop.views.products'))

@login_required
def remove_from_cart(request, object_id):
    product = Product.objects.get(id=object_id)
    cart = Cart(request)
    cart.remove(product)
    
    return HttpResponseRedirect(reverse('online_order.views.order_online'))

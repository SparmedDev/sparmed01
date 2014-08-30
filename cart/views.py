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
    
    categories = Category.objects.all()    
    category = categories.get(slug=category_slug)  
    
    return HttpResponseRedirect(reverse('shop.views.products'))

@login_required
def remove_from_cart(request, object_id):
    product = Product.objects.get(id=object_id)
    if product:
        cart = Cart(request)
        cart.remove(product)
    
    return HttpResponseRedirect(reverse('online_order.views.order_online'))

@login_required
def set_quantity_on_product(request):
  if request.method == 'POST':
    for key, value in request.POST.iteritems():
      if value.isdigit():
        object_id = key.split('_')[0]
        if object_id.isdigit():
          product = Product.objects.get(id=object_id)
          if product:
            cart = Cart(request)
            cart.set_product_quantity(product, value)
    
    return HttpResponseRedirect(reverse('online_order.views.order_online'))
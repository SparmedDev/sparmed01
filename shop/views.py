from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

import json
from django.http import HttpResponse, HttpResponseRedirect
from haystack.query import SearchQuerySet

from shop.models import Product, Category, GenericForm
from cart import Cart

# Create your views here.
@never_cache
def products(request, slug="0"):
    categories = Category.objects.all()
    
    try:
        category = categories.get(slug=slug)    
    except Category.DoesNotExist:
        category = categories.get(id=1)     
        return HttpResponseRedirect(reverse('shop.views.products', kwargs={'slug':category.slug}))
  
    return render(request, 'shop/products.html', {'categories':categories, 'category':category})

@never_cache
def details(request, category_slug, product_slug):
  category = get_object_or_404(Category, slug=category_slug)
  product = category.products.get(slug=product_slug)
  images = product.images.all()

  return render(request, 'shop/details.html', {'category':category, 'product':product, 'images':images})

@never_cache
@login_required
def add_to_cart(request):
    if request.method == 'POST':
        form = GenericForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data.get('q')
            
            try:
                product = Product.objects.get(product_id=value)
            except Product.DoesNotExist:
                product = Product.objects.get(name=value)
                
            if product:
              cart = Cart(request)
              cart.add(product)    
            else:
              raise ValueError('Could not find product based on value: %s' % value)
        #else:
        #   raise ValueError('Form is invalid')
    else:
        raise ValueError('Cannot add to cart if request method is not POST')
      
    return HttpResponseRedirect(reverse('online_order.views.order_online'))      
        

@never_cache
@login_required
def autocomplete(request):
    sqs1 = SearchQuerySet().autocomplete(product_id_auto=request.GET.get('q', ''))[:5]
    sqs2 = SearchQuerySet().autocomplete(name_auto=request.GET.get('q', ''))[:5]
    
    suggestions1 = [result.product_id for result in sqs1]
    suggestions2 = [result.name for result in sqs2]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    suggestions = suggestions1 + suggestions2
    #suggestions = list(set(suggestions1 + suggestions2))
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')
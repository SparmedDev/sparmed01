from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

import json
from django.http import HttpResponse, HttpResponseRedirect, Http404
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
        category = get_object_or_404(Category, id=1)     
        return HttpResponseRedirect(reverse('shop.views.products', kwargs={'slug':category.slug}))
  
    return render(request, 'shop/products.html', {'categories':categories, 'category':category})

@never_cache
def details(request, category_slug, product_slug):
  category = get_object_or_404(Category, slug=category_slug)
  try:
      product = category.products.get(slug=product_slug)
  except Product.DoesNotExist:
      raise Http404
      
  images = product.images.all()

  return render(request, 'shop/details.html', {'category':category, 'product':product, 'images':images})

@never_cache
@login_required
def add_to_cart(request):
    if request.method == 'POST':
        form = GenericForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data.get('q')
            q_id = value.split(' ')[0]
            q_id = q_id.strip(' \t\n\r')  
            try:
                product = Product.objects.get(product_id=q_id)
            except Product.DoesNotExist:
                product = get_object_or_404(Product, slug=q_id.lower())
                
            cart = Cart(request)
            cart.add(product)    
      
    return HttpResponseRedirect(reverse('online_order.views.order_online'))      
             

@never_cache
@login_required
def autocomplete(request):    
    if request.method == 'GET':        
        query = request.GET.get('q', '')
      
        sqs_id = SearchQuerySet().autocomplete(product_id_auto=query)[:6]

        suggestions_id = ["%s - %s" % (result.product_id.strip(' \t\n\r') , result.name.strip(' \t\n\r') ) for result in sqs_id]
        suggestions_set = list(set(suggestions_id))
        
        cart = Cart(request)
        cart = cart.get_item_list()
        
        p_ids = ["{0} - {1}".format(p.product.product_id, p.product.name) for p in cart]

        suggestions = [s for s in suggestions_set if s not in p_ids]

        auto_data = json.dumps({
            'results': suggestions
        })

        return HttpResponse(auto_data, content_type='application/json')
    
    return HttpResponseRedirect(reverse('online_order.views.order_online'))    
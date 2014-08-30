from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import never_cache

from shop.models import Product, Category

# Create your views here.
@never_cache
def products(request, slug="0"):
    categories = Category.objects.all()
    
    try:
        category = categories.get(slug=slug)    
    except Category.DoesNotExist:
        category = categories.get(id=1)     
  
    return render(request, 'shop/products.html', {'categories':categories, 'category':category})

@never_cache
def details(request, category_slug, product_slug):
  category = get_object_or_404(Category, slug=category_slug)
  product = category.get(slug=product_slug)
  images = product.images.all()

  return render(request, 'shop/details.html', {'category':category, 'product':product, 'images':images})
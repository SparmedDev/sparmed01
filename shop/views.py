from django.shortcuts import render, get_object_or_404

from shop.models import Product, Category

# Create your views here.
def products(request, slug="0"):
    try:
        category = Category.objects.get(slug=slug)    
    except Category.DoesNotExist:
        category = Category.objects.get(id=1)
        
    categories = Category.objects.all()
  
    return render(request, 'shop/products.html', {'categories':categories, 'category':category})

def details(request, category_slug, product_slug):
  category = get_object_or_404(Category, slug=category_slug)
  product = get_object_or_404(Product, slug=product_slug)
  images = product.images.all()

  return render(request, 'shop/details.html', {'category':category, 'product':product, 'images':images})


def online_order(request):
  
  return render(request, 'shop/online_order_sheet.html')
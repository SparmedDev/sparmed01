from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from online_order.models import OrderForm

from shop.models import Category

# Create your views here.
@login_required
def online_order(request):  
    if request.method == 'POST':
        form = OrderForm(request.POST)
      
        if form.is_valid():
            print 'Form is valid'
    else:
        form = OrderForm()
        
    categories = Category.objects.all()
  
    return render(request, 'shop/online_order_sheet.html', {'form': form, 'categories':categories})
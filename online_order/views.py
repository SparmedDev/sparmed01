from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from online_order.models import OrderForm

from shop.models import Category

# Create your views here.
@login_required
def order_online(request):  
    if request.method == 'POST':
        form = OrderForm(request.POST)
      
        if form.is_valid():
            print 'Form is valid'
    else:
        form = OrderForm()
        
    categories = Category.objects.all()
  
    return render(request, 'online_order/online_order_sheet.html', {'form': form, 'categories':categories})
  
@login_required
def order_history(request):
  
  return render(request, 'online_order/order_history.html')
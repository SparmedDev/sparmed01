from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from online_order.models import OrderForm

# Create your views here.
@login_required
def online_order(request):  
    if request.method == 'POST':
        form = OrderForm(request.POST)
      
        if form.is_valid():
            print 'Form is valid'
    else:
        form = OrderForm()
  
    return render(request, 'shop/online_order_sheet.html', {'form': form})
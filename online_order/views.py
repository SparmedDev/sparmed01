from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache

from online_order.models import OrderForm, SparmedUser
from online_order.admin import SparmedUserChangeForm

from shop.models import Category
from cart import Cart

# Create your views here.
@login_required
@never_cache
def order_online(request):  
    if request.method == 'POST':
        form = OrderForm(request.POST)
      
        if form.is_valid():
            order = form.save(commit=False)
            order.set_cart(Cart(request))
            request.user.add_to_order_history(order)
            order.save()
    else:
        form = OrderForm()
        
    return render(request, 'online_order/online_order_sheet.html', {'form': form})
  
@login_required
def order_history(request):
  
  return render(request, 'online_order/order_history.html')


@login_required
@never_cache
def account_area(request, account_slug):  
  user = request.user
  
  if request.method == 'POST':
      form = SparmedUserChangeForm(request.POST, instance=user)
      if form.is_valid():
          form.save()
          return render(request, 'online_order/account_area.html', {'feedback':'Your account has been succesfully updated. Please wait a few minutes for the changes to take effect.'})
  else:
      form = SparmedUserChangeForm(instance=user)
  
  return render(request, 'online_order/account_area.html', {'form':form})

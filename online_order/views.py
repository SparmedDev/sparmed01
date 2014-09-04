from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache
from django.core.urlresolvers import reverse

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
            cart = Cart(request)
            
            if cart and order:
                request.user.add_to_order_history(order, cart)
                cart.clear()
              
                return HttpResponseRedirect(reverse('online_order.views.order_history'))              
            else:
                raise ValueError('Cannot order online and set cart when cart is null')          
        else:
            raise ValueError("Cannot order online, form is invalid")
    else:
        form = OrderForm()
        
    return render(request, 'online_order/online_order_sheet.html', {'form': form})
  
@login_required
@never_cache
def order_history(request):  
  orders = request.user.orders.all()
  
  return render(request, 'online_order/order_history.html', {'orders':orders})


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

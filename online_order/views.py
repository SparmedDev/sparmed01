from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from online_order.models import OrderForm, SparmedUser
from online_order.admin import SparmedUserChangeForm

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
        
    return render(request, 'online_order/online_order_sheet.html', {'form': form})
  
@login_required
def order_history(request):
  
  return render(request, 'online_order/order_history.html')


@login_required
def account_area(request, account_slug):  
  user = request.user
  
  if request.method == 'POST':
      form = SparmedUserChangeForm(request.POST)
  else:
      data = {'name':user.name, 'country':user.country, 'address':user.address, 'city':user.city, 'postal_code':user.postal_code, 'contact_person_name':user.contact_person_name, 'contact_telephone':user.contact_telephone, 'email':user.email, 'password':user.password}
      form = SparmedUserChangeForm(initial=data)
  
  return render(request, 'online_order/account_area.html', {'form':form})

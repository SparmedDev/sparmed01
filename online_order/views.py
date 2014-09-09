from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache
from django.core.urlresolvers import reverse

from online_order.models import OrderForm, SparmedUser, OrderHistoryItem
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
                new_order = request.user.add_to_order_history(order, cart)
                cart.clear()
              
                return HttpResponseRedirect(reverse('online_order.views.order_confirmation', kwargs={'order_id':new_order.pk, 'confirmed':False}))
                #return HttpResponseRedirect(reverse('online_order.views.order_history'))              
            else:
                raise ValueError('Cannot order online and set cart when cart is null')          
        else:
            raise ValueError("Cannot order online, form is invalid")
    else:
        form = OrderForm()
        
    return render(request, 'online_order/online_order_sheet.html', {'form': form})
  
@login_required  
@never_cache
def order_confirmation(request, order_id, confirmed):
    if confirmed == 'True':
        order = OrderHistoryItem.objects.get(pk=order_id)
        if order:
            recipients = [
            #{ 'email': 'info@sparmed.dk',
            #  'name': 'SparMed' },
            { 'email': order.user.email,
              'name': order.user.contact_person_name },
            ]  
          
            import os
            EMAIL_API_KEY = os.environ.get('MANDRILL_APIKEY')

            #import mandrill
            #try:
            #    mandrill_client = mandrill.Mandrill(EMAIL_API_KEY)
            #    message = {
            #        'from_email': 'info@sparmed.dk',
            #        'from_name': 'SparMED.dk',
            #        'subject': 'SparMED Order Receipt',
            #        'global_merge_vars': {'name':'order', 'content':order},
            #        'to': recipients,
             #       'inline_css':True,
            #    }
            #    mandrill_client.messages.send_template('online_order/order_confirmation', [], message)

            #except mandrill.Error, e:
            #    # Mandrill errors are thrown as exceptions
            #    print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
            #    raise

            pass
        else:
            raise ValueError('Cannot send order, order is not valid')
    else:
        order = OrderHistoryItem.objects.get(pk=order_id)
        if order:
            return render(request, 'online_order/order_confirmation.html', {'order':order})
        else:
            raise ValueError('Cannot render order confirmation without valid order object')
            
    raise ValueError('dropped through')
    
@login_required
def order_regret(request, order_id):
    order = OrderHistoryItem.objects.get(pk=order_id)
    if order:
        order.delete()
        return HttpResponseRedirect(reverse('online_order.views.order_online'))
    else:
        raise ValueError('Could not find requested order to delete')
    
  
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

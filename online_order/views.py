from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict  

from online_order.models import OrderForm, SparmedUser, OrderHistoryItem
from online_order.admin import SparmedUserChangeForm

from shop.models import Category, Product

from cart import Cart

from django.template.loader import render_to_string
import mandrill

from django.views.decorators.csrf import ensure_csrf_cookie

from django.core.cache import cache

# Create your views here.
@login_required
@never_cache
def order_online(request):  
    if request.method == 'POST':
        cart = Cart(request)
        if cart.count() <= 0:
            form = OrderForm()
            return render(request, 'online_order/online_order_sheet.html', {'form': form, 'order_feedback': 'error'})  
      
        form = OrderForm(request.POST)      
        if form.is_valid():
            order = form.save(commit=False)                      
            new_order = request.user.add_to_order_history(order, cart)              
            return HttpResponseRedirect(reverse('online_order.views.order_confirmation', kwargs={'order_id':new_order.pk, 'confirmed':False}))
    else:
        form = OrderForm()        
        
    #account_change = not request.session.get('removed_account_change_notice')
    account_change = not cache.get('removed_account_change_notice')
        
    return render(request, 'online_order/online_order_sheet.html', {'form': form, 'cookie_account_change': account_change })

@login_required
@ensure_csrf_cookie
def remove_account_change_cookie(request):
    if request.method == 'POST':
        #request.session['removed_account_change_notice'] = True
        cache.set('removed_account_change_notice', True)
      
    return HttpResponseRedirect(reverse('online_order.views.order_online'))
  
@login_required
@never_cache  
def reorder_online(request, order_pk):  
    user = request.user
    order = user.orders.get(pk=order_pk)
    if order:
        cart = Cart(request)
        if cart.count() > 0:
            cart.clear()           

        order_dict = model_to_dict(order)          
        form = OrderForm(initial=order_dict, auto_id=True)        
        
        for product in order.items.all():
            p = Product.objects.get(id=product.object_id)  
            cart.add(p, product.quantity)
    else:
        form = OrderForm()
        
    #account_change = not request.session.get('removed_account_change_notice')
    account_change = not cache.get('removed_account_change_notice')
    
    return render(request, 'online_order/online_order_sheet.html', {'form': form, 'cookie_account_change':account_change })
 
@login_required  
@never_cache
def order_print(request, order_id):
    order = OrderHistoryItem.objects.get(pk=order_id)
    return render(request, 'online_order/order_history_print.html', {'order':order})  
    
@login_required  
@never_cache
def order_confirmation(request, order_id, confirmed):
    order = OrderHistoryItem.objects.get(pk=order_id)
    if confirmed == 'True':        
        recipients = [
          { 'email': 'admin@SparMED.dk',
           'name': 'SparMED' },
          { 'email': order.user.email,
           'name': order.user.contact_person_name },
        ]            

        html_content = render_to_string('online_order/order_email.html', {'order':order})

        try:
          mandrill_client = mandrill.Mandrill('Bml5XQ7DhMZLvw3NDwykrQ')
          message = {
            'from_email': 'info@sparmed.dk',
            'from_name': 'SparMED.dk',
            'subject': 'Online Order Confirmation Receipt | SparMED',
            'html': html_content,
            'to': recipients,
            'headers': {"Reply-To": "info@sparmed.dk"},
            "auto_html": True,
            'inline_css': True,
            "metadata": {"website": "www.sparmed.dk"}, 
            "async": True,
          }
          result = mandrill_client.messages.send(message=message)

        except mandrill.Error, e:
          # Mandrill errors are thrown as exceptions
          print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
          pass      

        cart = Cart(request)
        cart.delete()
            
        return HttpResponseRedirect(reverse('online_order.views.order_history'))
    else:
        return render(request, 'online_order/order_confirmation.html', {'order':order})
            
    return HttpResponseRedirect(reverse('online_order.views.order_online'))
    
@login_required
def order_regret(request, order_id):
    order = OrderHistoryItem.objects.get(pk=order_id)
    order.delete()
        
    return HttpResponseRedirect(reverse('online_order.views.order_online'))
    
@login_required
@never_cache
def order_history(request):  
    orders = request.user.orders.all()
    return render(request, 'online_order/order_history.html', {'orders':orders})

@login_required
@never_cache
def account_area(request, account_slug):  
  if request.method == 'POST':
      form = SparmedUserChangeForm(request.POST, instance=request.user)
      if form.is_valid():
          form.save()
          return render(request, 'online_order/account_area.html', {'feedback':'Your account has been succesfully updated. Please wait a few seconds for the changes to take effect.'})
  else:
      form = SparmedUserChangeForm(instance=request.user)
  
  return render(request, 'online_order/account_area.html', {'form':form})

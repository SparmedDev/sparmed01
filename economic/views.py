from django.shortcuts import render
import requests

credentials = { 'appId': 'OxKf30TPeqqDj3JXyOKYcK027-wO5ydYvcMr08Q_B9M1', 'accessId': 'vshDszEegEPEpLm8_uV0NwVWtfOSlviMuUlmSBVxip01', 'Content-Type': 'application/json' }

def get_economic_url(url, usePageSize):
    economic_base_url = 'https://restapi.e-conomic.com'
    
    if usePageSize:
        return u"%s/%s/%s" % (economic_base_url, url, "?pagesize=999")
    else:
        return u"%s/%s" % (economic_base_url, url)
            
def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result      

# Create your views here.
def index(request):         
    customers_url = get_economic_url('customers', True)  
    products_url = get_economic_url('products', True)
    
    customers_r = requests.get(customers_url, params=credentials)        
    products_r = requests.get(products_url, params=credentials)
    return render(request, 'economic/index.html', {'customers': customers_r.json(), 'products': products_r.json() })
  
def customer(request, url):
    r = requests.get(url)
    r_json = r.json()
        
    invoices_url = get_economic_url("invoices-experimental", False)
    invoices = requests.get(invoices_url, params=credentials)
    invoices_json = invoices.json()   
    
    invoices_drafts = requests.get(invoices_json["drafts"])
    invoices_booked = requests.get(invoices_json["booked"])
    invoices_overdue = requests.get(invoices_json["overdue"])
    invoices_totals = requests.get(invoices_json["totals"])
    invoices_unpaid = requests.get(invoices_json["unpaid"])
    
    #invoices = merge_dicts(invoices_drafts.json(), invoices_booked.json(), invoices_overdue.json(), invoices_totals.json(), invoices_unpaid.json())
    
    accounts = requests.get(get_economic_url("accounts", True), params=credentials)
    
    
    return render(request, 'economic/customer.html', {'customer': r_json, 'invoices_drafts': invoices_drafts.json(), 'invoices_booked': invoices_booked.json(), 'invoices_overdue': invoices_overdue.json(), "invoices_totals": invoices_totals.json(), "invoices_unpaid": invoices_unpaid.json(), 'invoices': invoices_json, 'accounts': accounts.json() })
  
def product(request, url):
    r = requests.get(url)
    return render(request, 'economic/product.html', {'product': r.json() })
from django.shortcuts import render
import requests

credentials = { 'appId': 'OxKf30TPeqqDj3JXyOKYcK027-wO5ydYvcMr08Q_B9M1', 'accessId': 'vshDszEegEPEpLm8_uV0NwVWtfOSlviMuUlmSBVxip01', 'Content-Type': 'application/json' }
economic_base_url = 'https://restapi.e-conomic.com/'

def get_economic_url(url):
  return u"%s%s%s" % (economic_base_url, url, "?pagesize=999")

# Create your views here.
def index(request):         
    customers_url = get_economic_url('customers')  
    products_url = get_economic_url('products')
    
    customers_r = requests.get(customers_url, params=credentials)        
    products_r = requests.get(products_url, params=credentials)
    return render(request, 'economic/index.html', {'customers': customers_r.json(), 'products': products_r.json() })
  
def customer(request, url):
    r = requests.get(url)
    r_json = r.json()
        
    invoices_url = get_economic_url("INVOICES-EXPERIMENTAL/DRAFTS")
    invoices = requests.get(invoices_url, params=credentials)
    invoices_json = invoices.json()   
    
    
    return render(request, 'economic/customer.html', {'customer': r_json, 'invoice': invoices_json })
    #return render(request, 'economic/customer.html', {'customer': r_json })
  
def product(request, url):
    r = requests.get(url)
    return render(request, 'economic/product.html', {'product': r.json() })
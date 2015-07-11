from django.shortcuts import render
import requests

credentials = { 'appId': 'OxKf30TPeqqDj3JXyOKYcK027-wO5ydYvcMr08Q_B9M1', 'accessId': 'vshDszEegEPEpLm8_uV0NwVWtfOSlviMuUlmSBVxip01', 'Content-Type': 'application/json' }

# Create your views here.
def index(request):         
    customers_url = 'https://restapi.e-conomic.com/customers?pagesize=999'  
    products_url = 'https://restapi.e-conomic.com/products?pagesize=999'
    
    customers_r = requests.get(customers_url, params=credentials)        
    products_r = requests.get(products_url, params=credentials)
    return render(request, 'economic/index.html', {'customers': customers_r.json(), 'products': products_r.json() })
  
def customer(request, url):
    r = requests.get(url)
    r_json = r.json()
        
    invoice = requests.get(r_json.invoice)
    
    return render(request, 'economic/customer.html', {'customer': r_json, 'invoice': invoice.json() })
  
def product(request, url):
    r = requests.get(url)
    return render(request, 'economic/product.html', {'product': r.json() })
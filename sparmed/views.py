from django.shortcuts import render
from news.models import NewsPost
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from shop.models import Category

def home(request):
  news_posts = NewsPost.objects.all()

  return render(request, "index.html", {'news_posts':news_posts})

def about(request):

  return render(request, "about.html")

def contact(request):

  return render(request, "contact.html")

def terms_conditions(request):
  
  return render(request, "terms_conditions.html")

def privacy_policy(request):
  
  return render(request, "privacy_policy.html")

#from suds.client import Client
@never_cache
@login_required
def inventory(request):
  categories = Category.objects.all()      
  
  #url = 'api.e-conomic.com/secure/api1/economicwebservice.asmx'
  #client = Client(url)

  return render(request, "inventory.html", {'categories':categories,})

@login_required
def distributor_login(request):
  
  return render(request, "distributor_login.html")
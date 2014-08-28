from django.shortcuts import render
from news.models import NewsPost
from django.contrib.auth.decorators import login_required

def home(request):
  news_posts = NewsPost.objects.all()

  return render(request, "index.html", {'news_posts':news_posts})

def about(request):

  return render(request, "about.html")

def contact(request):

  return render(request, "contact.html")

def distributors(request):

  return render(request, "distributors.html")

@login_required
def distributor_login(request):
  
  return render(request, "distributor_login.html")
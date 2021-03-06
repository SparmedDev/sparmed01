from django.shortcuts import render
from news.models import NewsPost
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from index_page.models import IndexPageModel
from shop.models import Category

def home(request):
    news_posts = NewsPost.objects.all()
    page_model = IndexPageModel.objects.all().first()
    return render(request, "index.html", {'news_posts':news_posts, 'index_page_model':page_model })

def about(request):
    return render(request, "about.html")

def terms_conditions(request):
    return render(request, "terms_conditions.html")

def privacy_policy(request):
    return render(request, "privacy_policy.html")

@never_cache
@login_required
def inventory(request):
    categories = Category.objects.all()
    return render(request, "inventory.html", {'categories':categories,})

@login_required
def distributor_login(request):
    return render(request, "distributor_login.html")
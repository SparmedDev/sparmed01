from django.shortcuts import render
from distributors.models import Distributor

# Create your views here.
def distributors(request):
  
  distributors = Distributor.objects.all()

  return render(request, "distributors.html", {'distributors': distributors})
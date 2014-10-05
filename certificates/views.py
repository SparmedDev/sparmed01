from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from certificates.models import CertificateItem, CertificateSubgroup, CertificateGroup

# Create your views here.
@login_required
def certificates(request):
  
  return render(request, "certificates.html")
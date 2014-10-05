from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required

from certificates.models import CertificateGroup

# Create your views here.
@login_required
def certificates(request):  
  groups = get_list_or_404(CertificateGroup)
  
  return render(request, "certificates.html", {'groups':groups})
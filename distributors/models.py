from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Distributor(models.Model):
    country = models.CharField(max_length=255, verbose_name=_("Country Name"))
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
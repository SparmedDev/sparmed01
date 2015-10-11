from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)

# Create your models here.
class IndexPageModel(models.Model):
    slogan = models.CharField(max_length=255, verbose_name=_("Index Page Slogan"), null=True, blank=True)

    def __unicode__(self):
      return u'%s' % self.slogan

    def clean(self):
        validate_only_one_instance(self)
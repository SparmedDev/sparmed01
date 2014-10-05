from django.db import models
import datetime
from validatedfile.fields import ValidatedFileField

class CertificateItem(models.Model):
    title = models.CharField(max_length=255, verbose_name="Certificate/Document Title")
    document = ValidatedFileField(blank=True, null=True, verbose_name="PDF Document file (256 MB max)", upload_to='/certificates/', content_types=['application/pdf'], max_upload_size=1024*1024*256)
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date and time added")
    
    subgroup = models.ForeignKey('CertificateSubgroup', related_name='products')
    group = models.ForeignKey('CertificateGroup', related_name='products')
    
    class Meta:
        ordering = ['order_index', 'added']
        
    def __unicode__(self):
       return u'%s' % self.title        
    
class CertificateSubgroup(models.Model):
    title = models.CharField(max_length=255, verbose_name="Subgroup Title/Name")
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date and time added")
    
    group = models.ForeignKey('CertificateGroup', related_name='subgroups', verbose_name="Associated Group")
    
    class Meta:
        ordering = ['order_index', 'added'] 
        
    def __unicode__(self):
       return u'%s' % self.title               
  
class CertificateGroup(models.Model):
    title = models.CharField(max_length=255, verbose_name="Group Title/Name")
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)  
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date and time added")
    
    class Meta:
        ordering = ['order_index', 'added']    
        
    def __unicode__(self):
       return u'%s' % self.title               
    
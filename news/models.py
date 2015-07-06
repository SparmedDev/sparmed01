from django.db import models
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class NewsImage(models.Model):
    image_title = models.CharField(max_length=200, verbose_name=_("Picture Title"), blank=True)
    image = ImageField(upload_to="/media/news")
    news_post = models.ForeignKey('NewsPost', related_name="images", verbose_name=_("Associated News Post"))

    def get_absolute_url(self):
      return u'%s' % self.image.url

    def __unicode__(self):
      return u'%s' % self.image_title
    
class NewsPost(models.Model):
  title = models.CharField(max_length=60)
  added = models.DateTimeField(default=timezone.now, verbose_name=_("Date and time added"))
  content = RichTextField(verbose_name=_("Write your news post here (Please do not attempt to insert images here, instead use the news image below)"), blank=True, null=True)
  slug = models.SlugField(unique=True, max_length=255, verbose_name=_("URL; Never modify this value!"))
  
  def __unicode__(self):
    return self.title
  
  class Meta:
    ordering = ['-added']
    
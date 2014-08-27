from django.db import models
from sorl.thumbnail import ImageField
import datetime

class NewsImage(models.Model):
    image_title = models.CharField(max_length=200, verbose_name="Picture Title", blank=True)
    image = ImageField(upload_to="/media/news")
    news_post = models.ForeignKey('NewsPost', related_name="images", verbose_name="Associated News Post")

    def get_absolute_url(self):
      return u'%s' % self.image.url

    def __unicode__(self):
      return u'%s' % self.image_title
    
class NewsPost(models.Model):
  title = models.CharField(max_length=60)
  added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date and time added")
  content = models.TextField(default="Write your news post here", verbose_name="News Post Text Content")
  slug = models.SlugField(unique=True, max_length=255, verbose_name="URL; Never modify this value!")
  
  def __unicode__(self):
    return self.title
  
  class Meta:
    ordering = ['-added']
    
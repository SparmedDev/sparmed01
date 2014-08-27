from django.conf.urls import patterns, include, url
from django.contrib import sitemaps
from django.contrib.sitemaps import GenericSitemap

from sparmed import views
from shop import Product, Category

from django.contrib import admin
admin.autodiscover()

class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.6
    changefreq = 'daily'

    def items(self):
        return ['products', 'distributors', 'contact', 'about', 'home']

    def location(self, item):
        return reverse(item)
      
product_dict = {
    'queryset': Product.objects.all(),
    'date_field': 'added',
}

category_dict = {
    'queryset': Category.objects.all(),
    'date_field': 'added',
}

sitemaps = {
    'static': StaticViewsSitemap,
    'products': GenericSitemap(product_dict, priority=0.2),
    'categories': GenericSitemap(category_dict, priority=0.3),
}
      
urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       url(r'about/$', views.about, name='about'),

                       url(r'^contact/$', 'contact.views.contact', name='contact'),
                       url(r'^thanks/$', 'contact.views.thanks', name='thanks'),

                       url(r'^products/(?P<category_slug>[\w\-]+)/(?P<product_slug>[\w\-]+)/$', 'shop.views.details'),
                       url(r'^products/(?P<slug>[\w\-]+)/$', 'shop.views.products'),
                       url(r'^products/$', 'shop.views.products', name='products'),

                       url(r'distributors/$', views.distributors, name='distributors'),

                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
                       url(r'^robots\.txt$', include('robots.urls')),
                      )

from django.conf.urls import patterns, include, url
from django.contrib import sitemaps
from django.contrib.sitemaps import GenericSitemap
from django.core.urlresolvers import reverse

from sparmed import views
from shop.models import Product, Category

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
                       url(r'distributors/$', views.distributors, name='distributors'),

                       url(r'^contact/$', 'contact.views.contact', name='contact'),
                       url(r'^thanks/$', 'contact.views.thanks', name='thanks'),
                       
                       #url(r'^distributor_login/$', 'distributor_login.views.distributor_login', name='distributor_login', {'template_name': 'distributor_login/index.html'}),
                       url(r'^distributor-login/$', views.distributor_login, name='distributor-login'),
                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),

                       url(r'^products/(?P<category_slug>[\w\-]+)/(?P<product_slug>[\w\-]+)/$', 'shop.views.details'),
                       url(r'^products/(?P<slug>[\w\-]+)/$', 'shop.views.products'),
                       url(r'^products/$', 'shop.views.products', name='products'), 
                       
                       url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/'}, name="password_reset"),
                       url(r'^user/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
                       url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/user/password/done/'}),
                       url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),                       

                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
                       url(r'^robots\.txt$', include('robots.urls')),
                      )

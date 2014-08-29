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

                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),

                       url(r'^distributor_login/account_area/(?P<account_slug>[\w\-]+)/$', 'online_order.views.account_area', name='account-area'),
                       url(r'^distributor_login/order_history/$', 'online_order.views.order_history', name='order-history'),
                       url(r'^distributor_login/order_online/$', 'online_order.views.order_online', name='order-online'),
                       url(r'^distributor_login/certificates/$', views.certificates, name='certificates'),
                       url(r'^distributor_login/inventory/$', views.inventory, name='inventory'),                        
                       url(r'^distributor-login/$', views.distributor_login, name='distributor-login'),                       

                       url(r'^products/(?P<category_slug>[\w\-]+)/(?P<product_slug>[\w\-]+)/$', 'shop.views.details'),
                       url(r'^products/(?P<slug>[\w\-]+)/$', 'shop.views.products'),
                       url(r'^products/$', 'shop.views.products', name='products'), 
                       
                       url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/'}, name="password_reset"),
                       url(r'^user/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
                       url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/user/password/done/'}, name='password_reset_confirm'),
                       url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),                       

                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
                       url(r'^robots\.txt$', include('robots.urls')),
                      )

from django.conf.urls import patterns, include, url
from django.contrib import sitemaps
from django.contrib.sitemaps import GenericSitemap
from django.core.urlresolvers import reverse
from django.conf.urls.i18n import i18n_patterns

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

urlpatterns = [
  url(r'^clear_cart/$', 'cart.views.clear_cart', name='clear-cart'),
  url(r'^add_to_cart/$', 'cart.views.add_to_cart', name='add-to-cart'),
  url(r'^remove_from_cart/(?P<object_id>[0-9]+)/$', 'cart.views.remove_from_cart', name='remove-from-cart'),
  url(r'^set_quantity_cart/$', 'cart.views.set_quantity_on_product', name='set-quantity-cart'),

  url(r'^cookies/remove_account_change/$', 'online_order.views.remove_account_change_cookie', name='remove-account-change-cookie'),

#  url(r'^economic/list/$', 'economic.views.index', name='economic-index'),
#  url(r'^economic/customers/(?P<url>.*)/$', 'economic.views.customer', name='economic-customer'),
#  url(r'^economic/products/(?P<url>.*)/$', 'economic.views.product', name='economic-product'),

  url(r'^accounts/', include('authtools.urls')),

  url(r'^grappelli/', include('grappelli.urls')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^i18n/', include('django.conf.urls.i18n')),
  url(r'^translate/', include('rosetta.urls')),

  url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
  url(r'^robots\.txt$', include('robots.urls')),
]

distributor_login_patterns = [
  url(r'^account-area/(?P<account_slug>[\w\-]+)/$', 'online_order.views.account_area', name='account-area'),
  url(r'^order-history/re-order/(?P<order_pk>[0-9]+)/$', 'online_order.views.reorder_online', name='re-order-history'),
  url(r'^order-history/print/(?P<order_id>[0-9]+)/$', 'online_order.views.order_print', name='order-print'),
  url(r'^order-history/$', 'online_order.views.order_history', name='order-history'),
  url(r'^order-online/$', 'online_order.views.order_online', name='order-online'),
  url(r'^order-confirmation/(?P<order_id>[0-9]+)/(?P<confirmed>[\w\-]+)/$', 'online_order.views.order_confirmation', name='order-confirmation'),
  url(r'^order-regret/(?P<order_id>[0-9]+)/$', 'online_order.views.order_regret', name='order-regret'),

  url(r'^certificates/$', 'certificates.views.certificates', name='certificates'),
  url(r'^inventory/$', views.inventory, name='inventory'),
  url(r'^$', views.distributor_login, name='distributor-login'),
]

urlpatterns += i18n_patterns(
  url(r'^$', views.home, name='home'),
  url(r'^about/$', views.about, name='about'),
  url(r'^distributors/$', 'distributors.views.distributors', name='distributors'),

  url(r'^contact/$', 'contact.views.contact', name='contact'),
  url(r'^thanks/$', 'contact.views.thanks', name='thanks'),

  url(r'^distributor-login/', include(distributor_login_patterns, namespace='')),

  url(r'^products/(?P<category_slug>[\w\-]+)/(?P<product_slug>[\w\-]+)/$', 'shop.views.details'),
  url(r'^products/(?P<slug>[\w\-]+)/$', 'shop.views.products'),
  url(r'^products/$', 'shop.views.products', name='products'),

  url(r'^search/add_to_cart/$', 'shop.views.autocomplete_add_to_cart', name='add-to-cart-search'),
  url(r'^search/autocomplete/', 'shop.views.autocomplete', name='autocomplete-url'),
  url(r'^search/', include('haystack.urls'), name='search'),

  url(r'^privacy-policy/$', views.privacy_policy, name='privacy-policy'),
  url(r'^terms-conditions/$', views.terms_conditions, name='terms-conditions'),

  url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
  url('^', include('django.contrib.auth.urls')),
)

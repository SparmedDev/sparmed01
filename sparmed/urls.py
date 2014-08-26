from django.conf.urls import patterns, include, url

from sparmed import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home),
                       
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
                                            
    url(r'^robots\.txt$', include('robots.urls')),
)

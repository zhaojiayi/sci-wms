from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fvcom_stovepipe.views.fvDo'),
     
    url(r'^docs/', 'fvcom_stovepipe.views.documentation'),
    #url(r'^test/', 'fvcom_stovepipe.views.test'),
    url(r'^wms/(?P<dataset>.*)/', 'fvcom_stovepipe.views.wms'),
    #url(r'^populate/', 'fvcom_stovepipe.views.populate'),
    url(r'^wmstest/$', 'fvcom_stovepipe.views.wmstest'),
    url(r'^wmstest/openlayers/(?P<filepath>.*)', 'fvcom_stovepipe.views.openlayers'),
    url(r'^crossdomain.xml', 'fvcom_stovepipe.views.crossdomain'),    

    # url(r'^fvcom_compute/', include('fvcom_compute.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    )
    


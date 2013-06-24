# Django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
# Local imports
from dailydevs.views import display_devotion


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fiveq_test.views.home', name='home'),
    # url(r'^fiveq_test/', include('fiveq_test.foo.urls')),
    url(r'^devotion/(?P<input_date>\d{4}-\d{2}-\d{2})/$',
        display_devotion, name='display_devotion'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

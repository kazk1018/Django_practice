from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_practice.views.home', name='home'),
    # url(r'^Django_practice/', include('Django_practice.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # helloworld
    url(r'^$', 'helloworld.views.main'),

    # poils
    url(r'^polls/$', 'poils.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'poils.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'poils.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'poils.views.vote'),
)

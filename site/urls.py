from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin


urlpatterns = patterns('',
    (r'^api/locksmith/', include('locksmith.auth.urls')),
    (r'^api/', include('billy.site.api.urls')),
    (r'^browse/', include('billy.site.browse.urls')),
    (r'^data/(?P<state>\w\w).zip$', 'billy.site.api.views.data_zip'),
    (r'^status/$', 'django.views.generic.simple.redirect_to',
     {'url':'http://spreadsheets.google.com/ccc?key=tzA6I1Rmqh09Vkt40dRs-Rg'}),
    (r'^$', 'django.views.generic.simple.direct_to_template',
     {'template':'index.html'}),
    (r'^contributing/$', 'django.views.generic.simple.direct_to_template',
     {'template':'contributing.html'}),
    (r'^thanks/$', 'django.views.generic.simple.direct_to_template',
     {'template':'thankyou.html'}),
    (r'^status-test/$', 'billy.site.browse.views.all_states',
     {'template':'status.html'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT,
          'show_indexes': True}))
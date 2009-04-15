from django.conf.urls.defaults import *

import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import os
urlpatterns = patterns('',
    # Example:
    # (r'^talkboard/', include('talkboard.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^site-media/(.*)$', 'django.views.static.serve', {'document_root': 'media'}),

    #(r'^log/', include('web.log.URLconf')),
    (r'^favorites/add', 'favorites.views.index'),
    (r'^favorites/save', 'favorites.views.save_favorites'),
    (r'^favorites/delete', 'favorites.views.delete_favorites'),
    (r'^$', 'home.views.index'),
)

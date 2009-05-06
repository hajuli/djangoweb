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
    (r'^favorite/site-media/(.*)$', 'django.views.static.serve', {'document_root': 'media'}),

    #(r'^log/', include('web.log.URLconf')),
    (r'^favorite/favorites/add', 'favorites.views.index'),
    (r'^favorite/favorites/save', 'favorites.views.save_favorites'),
    (r'^favorite/favorites/delete', 'favorites.views.delete_favorites'),
    (r'^favorite/userpanel/', include('userpanel.URLconf')),
    (r'^favorite/$', 'home.views.index'),
)

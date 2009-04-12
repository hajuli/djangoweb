# coding=utf-8

import os, sys, logging
from google.appengine.ext.webapp import util
for k in [k for k in sys.modules if k.startswith('django')]:
    del sys.modules[k]

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch.dispatcher

def log_exception(*args, **kwds):
    logging.exception('Exception in request:')
    
django.dispatch.dispatcher.connect(
    log_exception, django.core.signals.got_request_exception)

django.dispatch.dispatcher.disconnect(
    django.db._rollback_on_exception,
    django.core.signals.got_request_exception)

def main():
    application = django.core.handlers.wsgi.WSGIHandler()
    util.run_wsgi_app(application)
    
if "__main__" == __name__:
    main()
    
    
    


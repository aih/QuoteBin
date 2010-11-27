import os
import sys
import site

prev_sys_path = list(sys.path)

new_sys_path = []
#site.addsitedir('/srv/python-environments/quotebinenv/lib/python2.6/site-packages/')
for item in list(sys.path):
    if item not in prev_sys_path:
       new_sys_path.append(item)
       sys.path.remove(item)
sys.path[:0] = new_sys_path

# this will also be different for each project!
sys.path.append('/home/django/domains/quotebin.com/quotebin')

os.environ['PYTHON_EGG_CACHE'] = '/home/django/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

sys.stdout=sys.stderr

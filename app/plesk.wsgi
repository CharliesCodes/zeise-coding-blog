#!/usr/bin/env python
import os
import sys

sys.path.append("/var/www/vhosts/zeise-coding.de/httpdocs/app");

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin
from mezzanine.core.views import direct_to_template
from questions import urls as q_urls
 
admin.autodiscover()

# Add the urlpatterns for any custom Django applications here. 
# You can also change the ``home`` view to add your own functionality to 
# the project's homepage.
urlpatterns = patterns("",
    ("^admin/", include(admin.site.urls)),
    url(r"^$", 'ekipeo.views.home', name="home"),
    ("^questions/", include(q_urls)),
    ("^", include("mezzanine.urls")),
)

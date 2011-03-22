
from django.conf.urls.defaults import *

urlpatterns = patterns("",
    (r'^(?P<slug>[a-z-]+)/$', "questions.views.detail"),
)

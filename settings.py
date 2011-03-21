# -*- coding:utf-8 -*-


######################
# MEZZANINE SETTINGS #
######################

# The following Mezzanine settings are already defined in 
# mezzanine.conf.defaults, but can be uncommented below in 
# order to override their defaults.

# Name of the current theme to host during theme development.
THEME = "darkbleu"

# Controls the ordering and grouping of the admin menu. 
# ADMIN_MENU_ORDER = (
#     (_("Content"), ("pages.Page", "blog.BlogPost", "blog.Comment",
#         (_("Media Library"), "fb_browse"),)),
#     (_("Site"), ("sites.Site", "redirects.Redirect", "conf.Setting")),
#     (_("Users"), ("auth.User", "auth.Group",)),
# )

# A three item sequence, each containing a sequence of template tags 
# used to render the admin dashboard.
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("blog_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )


########################
# MAIN DJANGO SETTINGS #
########################

DEBUG = False
DEV_SERVER = True

TEMPLATE_DEBUG = DEBUG
SERVER_EMAIL = 'web@lepoc.org'
DEFAULT_FROM_EMAIL = 'web@lepoc.org'

ADMINS = (
    ('Dominique Guardiola', 'web@quinode.fr'),
)

TIME_ZONE = "Europe/Paris"
LANGUAGE_CODE = 'fr-FR'
SITE_ID = 1

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CHARSET='utf-8'


USE_I18N = True
USE_L10N = True


# Make this unique, and don't share it with anybody.
SECRET_KEY = "f991a3e3-b6e7-4f94-a477-e6bcab1a32a2cf0e8b20-b0c1-4855-b249-7fd1c993c811906f1c33-447f-4ad0-8683-bc8455dffb1a"

# Tuple of IP addresses, as strings, that:
#   * See debug comments, when DEBUG is true
#   * Receive x-headers
INTERNAL_IPS = ("127.0.0.1",)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)


#############
# DATABASES #
#############

DATABASES = {
    "default": {
        # "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "ENGINE": "",
        # DB name or path to database file if using sqlite3.
        "NAME": "",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
         # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}


#########
# PATHS #
#########

import os

# Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Name of the directory for the project.
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]

# Every cache key will get prefixed with this value - here we set it to 
# the name of the directory the project is in to try and use something 
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = "/media/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/site_media/"

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(PROJECT_ROOT, MEDIA_URL.strip("/"))

# Package/module name to import the root urlpatterns from for the project.
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

LOGIN_URL = "/admin/"


################
# APPLICATIONS #
################

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.pages",
    "mezzanine.twitter",
)

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "mezzanine.conf.context_processors.settings",
)

# List of middleware classes to use. Order is important; in the request phase,
# this middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.DeviceAwareUpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "mezzanine.core.middleware.DeviceAwareFetchFromCacheMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelector",
)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"


#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    "debug_toolbar",
    "south",
    "django_extensions",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}


##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be 
# ignored in your version control system allowing for settings to be 
# defined per machine.
try:
    from local_settings import *
except ImportError:
    pass


####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been 
# defined so far, in order to provide some better defaults where 
# applicable.
from mezzanine.utils.conf import set_dynamic_settings
set_dynamic_settings(globals())
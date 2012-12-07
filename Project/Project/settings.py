# Django settings for Project project.
# EDITING by Kai Peng

#Superuser:
#Login: admin
#Password: password

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Kai Peng', 'kaipeng@seas.upenn.edu'),
)

MANAGERS = ADMINS

ROOT_DOMAIN = "http://ec2-23-20-199-2.compute-1.amazonaws.com"

AUTH_PROFILE_MODULE = 'pytrader.UserProfile'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangostack',
        'HOST': '/opt/bitnami/postgresql',
        'PORT': '5432',
        'USER': 'bitnami',
        'PASSWORD': 'c650e6e69e'
    }
}

EXAMPLE_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Detroit'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+qm--)y8b=qu-3h#x7=*h@mqjk+55u37(g-i0*h$j6^(2ck&amp;7g'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'Project.wsgi.application'
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	'/home/bitnami/apps/django/django_projects/Project/Templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    
    #User Installed Apps:
    'polls',
    'ajax_select',
    'example',
    'auth',
    'pytrader',
    'django_evolution',
    
    'django_tables2',
)

# DEFINE THE SEARCH CHANNELS:

AJAX_LOOKUP_CHANNELS = {
    #   pass a dict with the model and the field to search against

    # simplest way, automatically construct a search channel by passing a dictionary
    'label'  : {'model':'example.label', 'search_field':'name'},
    
    # Custom channels are specified with a tuple
    # channel: ( module.where_lookup_is, ClassNameOfLookup )
    'person' : ('example.lookups', 'PersonLookup'),
    'group'  : ('example.lookups', 'GroupLookup'),
    'song'   : ('example.lookups', 'SongLookup'),
    'cliche' : ('example.lookups','ClicheLookup')
}

# magically include jqueryUI/js/css

AJAX_SELECT_BOOTSTRAP = True
# True: [easiest]
#   use the admin's jQuery if present else load from jquery's CDN
#   use jqueryUI if present else load from jquery's CDN
#   use jqueryUI theme if present else load one from jquery's CDN
# False/None/Not set: [default]
#   you should include jQuery, jqueryUI + theme in your template


AJAX_SELECT_INLINES = 'inline'
# 'inline': [easiest]
#   includes the js and css inline
#   this gets you up and running easily
#   but on large admin pages or with higher traffic it will be a bit wasteful.
# 'staticfiles':
#   @import the css/js from {{STATIC_URL}}/ajax_selects using django's staticfiles app
#   requires staticfiles to be installed and to run its management command to collect files
#   this still includes the css/js multiple times and is thus inefficient
#   but otherwise harmless
# False/None: [default]
#   does not inline anything. include the css/js files in your compressor stack
#   or include them in the head of the admin/base_site.html template
#   this is the most efficient but takes the longest to configure

# when using staticfiles you may implement your own ajax_select.css and customize to taste



###########################################################################

#  STANDARD CONFIG SETTINGS ###############################################


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'python.trader@gmail.com'
EMAIL_HOST_PASSWORD = 'python192'
DEFAULT_FROM_EMAIL = 'accounts@pythontrader.com'

LOGIN_URL = '/Project/accounts/login'
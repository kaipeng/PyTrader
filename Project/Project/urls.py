#EDITING
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import *
from ajax_select import urls as ajax_select_urls

from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Project.views.home', name='home'),
    # url(r'^Project/', include('Project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^example/', include('example.urls')),


	
	# Authentication URLs
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/',  include('auth.urls')), 
    
    
	#####CUSTOM#####
	# Home Page
    url(r'^$', 'Project.views.index'),
    #url(r'^$',  direct_to_template,  {'template': 'base.html'},  name="index"), 
    
    ##Table Tester for Colin
    url(r'^trader/', include('table_test.urls')),

)
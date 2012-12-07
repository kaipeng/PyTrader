from django.conf.urls.defaults import *

from views import *
 
urlpatterns = patterns('',
    
	url(r'transactions/$',  transactions,  name="transactions"),
	url(r'positions/$', positions, name="positions"),
	url(r'orders/$', orders, name="orders"),

)
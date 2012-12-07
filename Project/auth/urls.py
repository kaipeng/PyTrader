from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout, \
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete, \
    password_change, password_change_done

from views import *
 
urlpatterns = patterns('',
    url(r'register/$',  register,  name="register"),
    url(r'activate/$',  activate,  name="activate"),
    url(r'logout/$',  logout,  name="logout"),
    url(r'login/$',  login,  name="login"),
    url(r'logout_success/$',  logout_success,  name="logout_success"),
    
    url(r'password_reset_done/$',  password_reset_done, name="password_reset_done"),
    url(r'password_reset_confirm/(?P<uidb36>\d+)/(?P<token>[^/]+?)/$',  password_reset_confirm, name="password_reset_confirm"),

    url(r'password_reset_confirm/',  password_reset_confirm, name="password_reset_confirm"),
    url(r'password_reset_complete/$',  password_reset_complete, name="password_reset_complete"),
    url(r'password_reset/$',  password_reset, name="password_reset"),

    url(r'password_change/$',  password_change, name="password_change"),
    url(r'password_change_done/$',  password_change_done, name="password_change_done"),  

    
    #TODO
    url(r'/$',  success,  name="success"),



)
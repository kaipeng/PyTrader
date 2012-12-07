from django.core.mail import send_mail
from hashlib import md5
from django.template import loader, Context
from Project.settings import ROOT_DOMAIN
import time

from django.contrib.auth.models import User


def send_activation(user):
    code = md5(user.username).hexdigest()
    url = ROOT_DOMAIN+"/Project/accounts/activate/?user=%s&code=%s" % (user.username, code)
    print(url)
    template = loader.get_template('registration/activation.html')
    context = Context({
        'username': user.username, 
        'url': url, 
    })
    send_mail('Activate your PyTrader Account', template.render(context), 'accounts@pytrader.com', [user.email])

def activate_user(username,  code):
    if code == md5(username).hexdigest():
        set_user_isactive(username)
        return True
    else:
        return False

def set_user_isactive(username):
    user = User.objects.get(username=username)
    user.is_active = True
    user.save()
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from pytrader.models import TraderProfile
from django.http import HttpResponseRedirect


from activation import send_activation
from threading import Thread

from table_test import sample_run as google


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", initial="username@gmail.com")
    #username = forms.CharField(label="Username")
    #password1 = forms.CharField( widget=forms.PasswordInput, label="Password")
    TRADING_EXPERIENCE_CHOICES = (
        ('1', 'What is a market?'),
        ('2', 'I read the WSJ'),
        ('3', 'I invest my own money'),
        ('4', 'Finance major'),
        ('5', 'Experienced investor'),
        ('6', 'Professional'),
    )
    
    TRADING_STYLE_CHOICES = (
        ('A', 'I Love Apple'),
        ('D', 'Day Trader'),
        ('V', 'Value Investor'),
        ('F', 'Fundamental Investor'),
        ('H', 'High Risk / High Leverage'),
        ('L', 'Long Only'),
        ('M', 'Momentum Trader'),
        ('E', 'Earnings Junkie'),
        ('W', 'Macro-Economic'),
        ('Q', 'Quantitative Analysis'),
        ('T', 'Technical Analysis'),
        ('S', 'Statistical Arbitrage'),
    )
    google_password = forms.CharField( widget=forms.PasswordInput, label="Google Account Password")
    trading_experience = forms.ChoiceField(label="Trading Experience", widget = forms.Select(), choices=TRADING_EXPERIENCE_CHOICES)
    trading_style = forms.ChoiceField(label="Trading Style", widget = forms.Select(), choices=TRADING_STYLE_CHOICES)
    avatar_url = forms.CharField(label="Avatar URL", initial="http://", required = False)

    class Meta:
        model = User
        fields = ("username", "email", 'password1')
        #exclude = ("user")
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            self.google_email = email
            return email
        raise forms.ValidationError("A user with that email address already exists.")
    
    #TODO - Check for validity of Google Account
    #TODO - Also set First/Last name of users

    def clean_google_password(self):
        password = self.cleaned_data["google_password"]
        try:
        	current_user = google.SampleRun(self.google_email, password)
        except:
            raise forms.ValidationError("Google Email or Password are not valid. ")
        """
        except:
        """
        return password
        
    #TODO - Set shit to Google Account
    def clean_avatar_url(self):
        avatar_url_data = self.cleaned_data["avatar_url"]
        if avatar_url_data == "http://":
            #fetch google
            pass
        return avatar_url_data
        
    def save(self):
        newuser = super(RegisterForm, self).save(commit=False)
        #newuser.is_active = False
        #newuser.save()
        cd = self.cleaned_data
        #newuser = User.objects.create_user(cd["username"], cd["email"], cd["password1"])
        newuser.is_active = False
        newuser.save()

        #Multithreading to send email
        thread = Thread(target=send_activation,  args=[newuser])
        thread.setDaemon(True)
        thread.start()

        
        uinfo = newuser.traderprofile_set.create()

        #get this from google
        #user.first_name = cd["FirstName"]
        #user.last_name = cd["LastName"]
        #user.save()
        #Save userinfo record
        #uinfo = user.get_profile()
        uinfo.google_password = cd["google_password"]
        uinfo.trading_experience = cd["trading_experience"]
        uinfo.trading_style = cd["trading_style"]
        uinfo.avatar_url = cd["avatar_url"]
        #uinfo.user = newuser  
        uinfo.save()
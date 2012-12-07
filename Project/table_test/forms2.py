#from django.contrib.auth.forms import UserCreationForm
from django import forms
#from django.contrib.auth.models import User

#from activation import send_activation
#from threading import Thread


class TxnForm(forms.Form):
	type = forms.ChoiceField(label="Transaction Type", widget = forms.Select(), choices=(('buy', 'Buy'), ('sell', 'Sell')))
	ticker = forms.CharField(label="Stock Symbol")
	quantity = forms.IntegerField(label="Quantity")
	price = forms.DecimalField(label="Price")

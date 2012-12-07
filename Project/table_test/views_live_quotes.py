# Create your views here.
#from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404

from forms2 import TxnForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from pytrader.models import TraderProfile


import django_tables2 as tables
#from django_tables2 import RequestConfig
import sample_run as google
import string
import datetime

#s = google.SampleRun('colin.schloss@gmail.com', 'oxbridge2')
#pfl = s.GetPortfolios(with_returns=True)[0]
portfolio_title = 'PyTrader 192'

def TransactionTable(s, pfl):
    table_list = []
    for pos in s.GetPositions(pfl, with_returns=True):
        pos_dict = {}
        pos_dict['name'] = pos.position_title
        pos_dict['symbol'] = FormatTicker(pos.ticker_id)
        for txn in s.GetTransactions(position=pos):
            d = txn.transaction_data
            txn_dict = {}
            txn_dict['type'] = d.type
            txn_dict['date'] = FormatDate(d.date)
            txn_dict['shares'] = d.shares
            txn_dict['price'] = d.price.money[0]
#            txn_dict['commission'] = d.commission.money[0]
            table_list.append(dict(pos_dict.items() + txn_dict.items()))
    return table_list

def PerformanceTable(s, pfl):
    table_list = []
    for pos in s.GetPositions(pfl, with_returns=True):
        d = pos.position_data
        pos_dict = {}
        pos_dict['name'] = pos.position_title
        pos_dict['symbol'] = FormatTicker(pos.ticker_id)
#        pos_dict['last_price'] = d.last_price
#        pos_dict['change'] = d.change
        pos_dict['shares'] = d.shares
        pos_dict['cost_basis'] = d.cost_basis
        pos_dict['mkt_value'] = d.market_value
        pos_dict['gain'] = d.gain
        pos_dict['gain_perc'] = d.gain_percentage
        pos_dict['days_gain'] = d.days_gain
        pos_dict['overall_return'] = d.return_overall
        table_list.append(pos_dict)
    return table_list

def FormatDate(date):
    return date[:string.find(date, 'T')]

def FormatTicker(ticker):
    return ticker[string.find(ticker, ':')+1:]

class TransactionView(tables.Table):
    name = tables.Column()
    symbol = tables.Column()
    type = tables.Column()
    date = tables.Column()
    shares = tables.Column()
    price = tables.Column()
#    commission = tables.Column()
    
class PerformanceView(tables.Table):
    name = tables.Column()
    symbol = tables.Column()
#    last_price = tables.Column()
#    change = tables.Column()
    shares = tables.Column()
    cost_basis = tables.Column()
    mkt_value = tables.Column()
    gain = tables.Column()
    gain_perc = tables.Column(verbose_name = 'gain %')
    days_gain = tables.Column(verbose_name = 'day\'s gain')
    overall_return = tables.Column()

#### VIEWS   ###

@login_required
def transactions(request):
    current_user_email = request.user.email
    current_user_password = TraderProfile.objects.get(user=request.user).google_password
    current_user = google.SampleRun(current_user_email, current_user_password)
    
    pfl = None
    for portfolio in current_user.GetPortfolios():
        if portfolio.portfolio_title == portfolio_title:
            pfl = portfolio
    if not pfl:
        pfl = current_user.AddPortfolio(portfolio_title, 'USD')
    
    txn_table = TransactionView(TransactionTable(current_user, pfl))
#    RequestConfig(request).configure(txn_table)
    return render(request, 'table_test/home.html', {'table': txn_table, 'name': 'Transactions'})

@login_required
def positions(request):

    current_user_email = request.user.email
    current_user_password = TraderProfile.objects.get(user=request.user).google_password
    current_user = google.SampleRun(current_user_email, current_user_password)
    
    pfl = None
    for portfolio in current_user.GetPortfolios():
        if portfolio.portfolio_title == portfolio_title:
            pfl = portfolio
    if not pfl:
        pfl = current_user.AddPortfolio(portfolio_title, 'USD')

    perf_table = PerformanceView(PerformanceTable(current_user, pfl))
#    RequestConfig(request).configure(txn_table)
    return render(request, 'table_test/home.html', {'table': perf_table, 'name': 'Positions'})

@login_required
def orders(request):
    csrf_context = RequestContext(request)
    current_user_email = request.user.email
    current_user_password = TraderProfile.objects.get(user=request.user).google_password
    current_user = google.SampleRun(current_user_email, current_user_password)
    
    pfl = None
    for portfolio in current_user.GetPortfolios():
        if portfolio.portfolio_title == portfolio_title:
            pfl = portfolio
    if not pfl:
        pfl = current_user.AddPortfolio(portfolio_title, 'USD')
        
    if request.method == 'POST': # If the form has been submitted...
        form = TxnForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            type = form.cleaned_data['type']
            ticker = form.cleaned_data['ticker']
            quantity = form.cleaned_data['quantity']
            #price = form.cleaned_data['price']
            """
            if type == 'buy':
                try:
                    current_user.Buy(pfl, 'NASDAQ:' + ticker, shares=quantity, price=price, date=datetime.datetime.now())
                except:
                    try:
                        current_user.Buy(pfl, 'NYSE:' + ticker, shares=quantity, price=price, date=datetime.datetime.now())
                    except:
                        return render_to_response("table_test/txn_failure.html", csrf_context)
            elif type == 'sell':
                try:
                    current_user.Sell(pfl, 'NASDAQ:' + ticker, shares=quantity, price=price, date=datetime.datetime.now())
                except:
                    try:
                        current_user.Sell(pfl, 'NYSE:' + ticker, shares=quantity, price=price, date=datetime.datetime.now())
                    except:
                        return render_to_response("table_test/txn_failure.html", csrf_context)
            """
            #confirm
            csrf_context = RequestContext(request, {'form': form, 'name': 'Place Order'})
            return render_to_response("table_test/txn_confirm.html", csrf_context)
    else:
        form = TxnForm() # An unbound form
    csrf_context = RequestContext(request, {'form': form, 'name': 'Place Order'})
    return render_to_response("table_test/txn.html", csrf_context)

@login_required
def confirm(request):
    csrf_context = RequestContext(request)
    current_user_email = request.user.email
    current_user_password = TraderProfile.objects.get(user=request.user).google_password
    current_user = google.SampleRun(current_user_email, current_user_password)
    
    pfl = None
    for portfolio in current_user.GetPortfolios():
        if portfolio.portfolio_title == portfolio_title:
            pfl = portfolio
    if not pfl:
        pfl = current_user.AddPortfolio(portfolio_title, 'USD')
        
    if request.method == 'POST': # If the form has been submitted...
        form = TxnForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            type = form.cleaned_data['type']
            ticker = form.cleaned_data['ticker']
            quantity = form.cleaned_data['quantity']
            
                        
            if type == 'buy':
                try:
                    current_user.Buy(pfl, 'NASDAQ:' + ticker, shares=quantity, price=price, date=datetime.datetime.now())
                except:
                    try:
                        current_user.Buy(pfl, 'NYSE:' + ticker, shares=quantity, price=price, date=datetime.datetime.now())
                    except:
                        return render_to_response("table_test/txn_failure.html", csrf_context)
            elif type == 'sell':
                try:
                    current_user.Sell(pfl, 'NASDAQ:' + ticker, shares=quantity, price=price, date=datetime.datetime.now())
                except:
                    try:
                        current_user.Sell(pfl, 'NYSE:' + ticker, shares=quantity, price=price, date=datetime.datetime.now())
                    except:
                        return render_to_response("table_test/txn_failure.html", csrf_context)
            #confirm
            csrf_context = RequestContext(request, {'form': form, 'name': 'Confirm Order'})
            return render_to_response("table_test/txn_success.html", csrf_context)
    else:
        #pull price
        c = GoogleFinanceAPI()
        try:
            price = c.get("NASDAQ:"+ticker)
        except:
            try:
                price = c.get("NYSE:"+ticker)
            except:
                price = 0
        cost = price*shares
        form = TxnForm() # An unbound form
    csrf_context = RequestContext(request, {'form': form, 'name': 'Confirm Order', 'price':price, 'cost':cost})
    return render_to_response("table_test/txn_confirm.html", csrf_context)
    
import urllib2
import json
import time

class GoogleFinanceAPI:
    def __init__(self):
        self.prefix = "http://finance.google.com/finance/info?client=ig&q="
    
    def get(self,symbol,exchange):
        url = self.prefix+"%s:%s"%(exchange,symbol)
        u = urllib2.urlopen(url)
        content = u.read()
        
        obj = json.loads(content[3:])
        return obj[0]
        


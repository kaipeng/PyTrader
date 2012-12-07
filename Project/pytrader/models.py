from django.db import models
from auth.models import *
from django.contrib.auth.models import User
from datetime import *
        
# Create your models here.
class TraderProfile(models.Model):
    #required by the auth model
    user = models.ForeignKey(User, unique=True)

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
    user = models.ForeignKey(User, unique=True)
    google_password = models.CharField(max_length=40, default='')
    avatar_url = models.CharField(max_length=200, default='')

    trading_experience = models.CharField(max_length=20, choices=TRADING_EXPERIENCE_CHOICES, default='')
    trading_style = models.CharField(max_length=20, choices=TRADING_STYLE_CHOICES, default='')

    # Portfolio Statistics
    trades = models.IntegerField(default = 0)
    cash_balance = models.DecimalField(decimal_places=2, max_digits=10, default = 0)
    long_stock_value = models.DecimalField(decimal_places=2, max_digits=10, default = 0)
    short_stock_value = models.DecimalField(decimal_places=2, max_digits=10, default = 0)
    portfolio_value = models.DecimalField(decimal_places=2, max_digits=10, default = 0)
    portfolio_beta = models.DecimalField(decimal_places=2, max_digits=10, default = 0)
    
    # Summary
    biggest_holding = models.CharField(max_length=40, default = 'n/a')
    biggest_winner = models.CharField(max_length=40, default = 'n/a')
    biggest_loser = models.CharField(max_length=40, default = 'n/a')

    #Trading Statistics
    annualized_yield = models.DecimalField(decimal_places=2, max_digits=10, default = 0)
    average_holding_period = models.DecimalField(decimal_places=2, max_digits=10, default = 0)
    average_trade_size = models.DecimalField(decimal_places=2, max_digits=10, default = 0)
    trade_frequency = models.DecimalField(decimal_places=2, max_digits=10, default = 0)
    
    def __unicode__(self):
        return self.user.username

# Current Holdings
class Position(models.Model):
    #Necessary
    identifier = models.CharField(max_length=40)
    symbol = models.CharField(max_length=40)
    
    realized_pnl = models.DecimalField(decimal_places=2, max_digits=10)
    unrealized_pnl = models.DecimalField(decimal_places=2, max_digits=10)
    is_open = models.BooleanField()
    
    date_opened = models.DateTimeField()
    date_closed = models.DateTimeField()
    last_traded = models.DateTimeField()

    trader_profile = models.ForeignKey(TraderProfile)
    def __unicode__(self):
        return self.identifier

# Transaction History
class Transaction(models.Model):
    identifier = models.CharField(max_length=40)
    symbol = models.CharField(max_length=40)
    date = models.DateTimeField()
    shares = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    commission = models.DecimalField(decimal_places=2, max_digits=10)

    trader_profile = models.ForeignKey(TraderProfile)
    def __unicode__(self):
        return self.identifier

# Likes (users to transactions)
class Like(models.Model):
    identifier = models.CharField(max_length=40)
    date = models.DateTimeField()
    transaction = models.ForeignKey(Transaction)
    trader_profile = models.ForeignKey(TraderProfile)
    def __unicode__(self):
        return self.identifier

# Dislikes (users to transactions)
class Dislike(models.Model):
    identifier = models.CharField(max_length=40)
    date = models.DateTimeField()
    transaction = models.ForeignKey(Transaction)
    trader_profile = models.ForeignKey(TraderProfile)
    def __unicode__(self):
        return self.identifier

# Follows (users to users)
class Follow(models.Model):
    identifier = models.CharField(max_length=40)
    date = models.DateTimeField()
    followee_username = models.CharField(max_length=40)
    trader_profile = models.ForeignKey(TraderProfile)
    def __unicode__(self):
        return self.identifier

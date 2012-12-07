# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TraderProfile'
        db.create_table('pytrader_traderprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('google_password', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('avatar_url', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('trading_experience', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
            ('trading_style', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
            ('trades', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cash_balance', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('long_stock_value', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('short_stock_value', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('portfolio_value', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('portfolio_beta', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('biggest_holding', self.gf('django.db.models.fields.CharField')(default='n/a', max_length=40)),
            ('biggest_winner', self.gf('django.db.models.fields.CharField')(default='n/a', max_length=40)),
            ('biggest_loser', self.gf('django.db.models.fields.CharField')(default='n/a', max_length=40)),
            ('last_trade', self.gf('django.db.models.fields.DateTimeField')()),
            ('annualized_yield', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('average_holding_period', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('average_trade_size', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('trade_frequency', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('pytrader', ['TraderProfile'])

        # Adding model 'Position'
        db.create_table('pytrader_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('realized_pnl', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('unrealized_pnl', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('is_open', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_opened', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_closed', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_traded', self.gf('django.db.models.fields.DateTimeField')()),
            ('trader_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pytrader.TraderProfile'])),
        ))
        db.send_create_signal('pytrader', ['Position'])

        # Adding model 'Transaction'
        db.create_table('pytrader_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('shares', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('commission', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('trader_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pytrader.TraderProfile'])),
        ))
        db.send_create_signal('pytrader', ['Transaction'])

        # Adding model 'Like'
        db.create_table('pytrader_like', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pytrader.Transaction'])),
            ('trader_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pytrader.TraderProfile'])),
        ))
        db.send_create_signal('pytrader', ['Like'])

        # Adding model 'Dislike'
        db.create_table('pytrader_dislike', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pytrader.Transaction'])),
            ('trader_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pytrader.TraderProfile'])),
        ))
        db.send_create_signal('pytrader', ['Dislike'])

        # Adding model 'Follow'
        db.create_table('pytrader_follow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('followee_username', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('trader_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pytrader.TraderProfile'])),
        ))
        db.send_create_signal('pytrader', ['Follow'])


    def backwards(self, orm):
        
        # Deleting model 'TraderProfile'
        db.delete_table('pytrader_traderprofile')

        # Deleting model 'Position'
        db.delete_table('pytrader_position')

        # Deleting model 'Transaction'
        db.delete_table('pytrader_transaction')

        # Deleting model 'Like'
        db.delete_table('pytrader_like')

        # Deleting model 'Dislike'
        db.delete_table('pytrader_dislike')

        # Deleting model 'Follow'
        db.delete_table('pytrader_follow')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 29, 22, 17, 41, 284515, tzinfo=<UTC>)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 29, 22, 17, 41, 284388, tzinfo=<UTC>)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pytrader.dislike': {
            'Meta': {'object_name': 'Dislike'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'trader_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pytrader.TraderProfile']"}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pytrader.Transaction']"})
        },
        'pytrader.follow': {
            'Meta': {'object_name': 'Follow'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'followee_username': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'trader_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pytrader.TraderProfile']"})
        },
        'pytrader.like': {
            'Meta': {'object_name': 'Like'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'trader_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pytrader.TraderProfile']"}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pytrader.Transaction']"})
        },
        'pytrader.position': {
            'Meta': {'object_name': 'Position'},
            'date_closed': ('django.db.models.fields.DateTimeField', [], {}),
            'date_opened': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'is_open': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_traded': ('django.db.models.fields.DateTimeField', [], {}),
            'realized_pnl': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'trader_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pytrader.TraderProfile']"}),
            'unrealized_pnl': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        'pytrader.traderprofile': {
            'Meta': {'object_name': 'TraderProfile'},
            'annualized_yield': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'avatar_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'average_holding_period': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'average_trade_size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'biggest_holding': ('django.db.models.fields.CharField', [], {'default': "'n/a'", 'max_length': '40'}),
            'biggest_loser': ('django.db.models.fields.CharField', [], {'default': "'n/a'", 'max_length': '40'}),
            'biggest_winner': ('django.db.models.fields.CharField', [], {'default': "'n/a'", 'max_length': '40'}),
            'cash_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'google_password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_trade': ('django.db.models.fields.DateTimeField', [], {}),
            'long_stock_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'portfolio_beta': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'portfolio_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'short_stock_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'trade_frequency': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'trades': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'trading_experience': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'trading_style': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'pytrader.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'commission': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'shares': ('django.db.models.fields.IntegerField', [], {}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'trader_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pytrader.TraderProfile']"})
        }
    }

    complete_apps = ['pytrader']

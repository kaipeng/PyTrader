from django.conf import settings
from django.core.management.base import NoArgsCommand
import MySQLdb

class Command(NoArgsCommand):
	help = "Drop and re-create the database"
	def handle_noargs(self, **options):
	
		print "Connecting..."
		db=MySQLdb.connect(host=settings.DATABASE_HOST or "localhost" ,user=settings.DATABASE_USER,
		passwd=settings.DATABASE_PASSWORD, port=int(settings.DATABASE_PORT or 3306))
		
		cursor = db.cursor()
		print "Dropping database %s" % settings.DATABASE_NAME
		cursor.execute("drop database %s; create database %s;" % (settings.DATABASE_NAME, settings.DATABASE_NAME))
		print "Dropped"
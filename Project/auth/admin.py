from pytrader.models import TraderProfile
from improved_admin_snippet import upgrade_user_admin

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms.models import inlineformset_factory


class TraderProfileFormSet(inlineformset_factory(User, TraderProfile)):
	def __init__(self, *args, **kwargs):
		super(TraderProfileFormSet, self).__init__(*args, **kwargs)
		self.can_delete = False

# Allow user profiles to be edited inline with User
class TraderProfileInline(admin.StackedInline):
	model = TraderProfile
	fk_name = 'user'
	max_num = 1
	extra = 0
	formset = TraderProfileFormSet

class MyUserAdmin(UserAdmin):
	inlines = [TraderProfileInline, ]
	actions = ['make_active', 'make_inactive',]
	list_filter = ['is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login',]
	list_display = ['first_name', 'last_name', 'email', 'username', 'last_login','is_active',]
	list_display_links = ['first_name', 'last_name', 'email', 'username']
	
	def make_active(self, request, queryset):
		rows_updated = queryset.update(is_active=True)
		if rows_updated == 1:
			message_bit = "1 person was"
		else:
			message_bit = "%s people were" % rows_updated
		self.message_user(request, "%s successfully made active." % message_bit)

	def make_inactive(self, request, queryset):
		rows_updated = queryset.update(is_active=False)
		if rows_updated == 1:
			message_bit = "1 person was"
		else:
			message_bit = "%s people were" % rows_updated
		self.message_user(request, "%s successfully made inactive." % message_bit)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
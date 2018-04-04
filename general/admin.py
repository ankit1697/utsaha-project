from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(DjangoUserAdmin):

	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'department')}),
		(('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   'groups', 'user_permissions')}),
		(('Academic Details'), {'fields': ('sem',)}),
		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
		(('Amount'), {'fields': ('amount',)})
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'password1', 'password2'),
		}),
	)

	list_display = ('username', 'first_name', 'last_name')
	search_fields = ('email', 'first_name', 'last_name')
	ordering = ('username',)


admin.site.register(Department)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Registration)
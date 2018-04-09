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
admin.site.register(Category)

class EventAdmin(admin.ModelAdmin):
    '''
        Admin View for Event
    '''
    list_display = ('name', 'price', 'coordinator')
    list_filter = ('price', 'date',)
    search_fields = ('name',)

admin.site.register(Event, EventAdmin)

class RegistrationAdmin(admin.ModelAdmin):
    '''
        Admin View for Registration
    '''
    list_display = ('event', 'payment', 'agent')
    list_filter = ('date_created','payment', 'agent')
    search_fields = ('agent','event',)

admin.site.register(Registration, RegistrationAdmin)
from django import forms
from general.models import Registration

from general.models import Event

class RegistrationForm(forms.ModelForm):
	event = forms.ModelChoiceField(queryset=Event.objects.filter(max_count__gt=0))
	class Meta:
		model = Registration
		exclude = ('agent', 'is_attended', 'code')
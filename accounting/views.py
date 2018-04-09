from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Finance
from general.models import Registration

# Create your views here.
class FinanceView(TemplateView):
	template_name = "accounting/finance.html"

	def get_context_data(self, **kwargs):
		context = super(FinanceView, self).get_context_data(**kwargs)
		context['finances'] = Finance.objects.all().order_by('-date')
		return context

	def get(self, request, *args, **kwargs):
		if request.user.groups.filter(name='Admin').exists():
			return super(FinanceView, self).get(request, *args, **kwargs)
		else:
			return HttpResponseRedirect(reverse_lazy('dashboard'))


class MarketingFinanceView(TemplateView):
	template_name = "accounting/marketing_finance.html"

	def get_context_data(self, **kwargs):
		context = super(MarketingFinanceView, self).get_context_data(**kwargs)
		registrations = Registration.objects.all()
		dates = list(set(registrations.values_list('date_created', flat=True)))
		agents = list(set(registrations.values_list('agent__first_name', flat=True)))
		context['dates'] = dates
		context['agents'] = agents
		context['registrations'] = Registration.objects.all()
		return context
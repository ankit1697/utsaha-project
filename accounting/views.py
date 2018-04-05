from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Finance

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

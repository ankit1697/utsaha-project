from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Finance

# Create your views here.
class FinanceView(TemplateView):
    template_name = "accounting/finance.html"

    def get_context_data(self, **kwargs):
        context = super(FinanceView, self).get_context_data(**kwargs)
        context['finances'] = Finance.objects.all().order_by('-date')
        return context
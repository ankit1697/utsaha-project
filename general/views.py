from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.db.models import Sum
from collections import Counter

from .models import Registration
from general.models import Category, Event

# Create your views here.
class IndexView(TemplateView):
	template_name = 'index.html'

class DashboardView(TemplateView):
    template_name = "marketing/dashboard.html"
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        leaderboard = Registration.objects.values('agent__username',).annotate(sum=Sum('event__price')).order_by('-sum')[:10]
        context['leaderboards'] = leaderboard
        return context

def event_scanner(request):
	return render(request, 'general/event_scanner.html')

def event_attended(request, code):
	event = Registration.objects.get(code=code)
	event.is_attended = True
	event.save()
	return HttpResponseRedirect(reverse_lazy("event_scanner"))

class CategoryListView(ListView):
	template_name = "general/category_list.html"
	model = Category
	context_object_name = "categories"

class EventListView(TemplateView):
	template_name = "general/event_list.html"
	
	def get_context_data(self, **kwargs):
	    context = super(EventListView, self).get_context_data(**kwargs)
	    category = Category.objects.get(pk=kwargs["pk"])
	    events = Event.objects.filter(category=category)
	    context['event_list'] = events
	    return context
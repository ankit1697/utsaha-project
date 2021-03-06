from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^event_list/(?P<pk>[\w\-]+)', views.EventListView.as_view(), name="event_list"),
	url(r'^category_list/', views.CategoryListView.as_view(), name="category_list"),
	url(r'^dashboard/', views.DashboardView.as_view(), name="dashboard"),
    url(r'^event_scanner/', views.event_scanner, name="event_scanner"),
	url(r'^event_attended/(?P<code>[\w\-]+)', views.event_attended, name="event_attended"),

	url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^year/2018', views.Year2018.as_view(), name="year_2018"),
	url(r'^year/2017', views.Year2017.as_view(), name="year_2017"),
]
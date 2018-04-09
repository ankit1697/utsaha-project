from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^finance', views.FinanceView.as_view(), name="finance"),
	url(r'^marketing_finance', views.MarketingFinanceView.as_view(), name="marketing_finance"),
]
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/',views.RegistrationView.as_view(), name="marketing_register"),
    url(r'^registration-list/',views.RegistraionListView.as_view(), name="registration_list"),
    # url(r'^send_event_mail/(?P<registration_pk>[\w\-]+)', views.send_event_mail, name="send_event_mail")
] 

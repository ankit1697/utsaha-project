from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib import messages


from general.models import Registration, Event
from .forms import RegistrationForm

import urllib.parse as ap
import urllib.request
from django.core.mail import send_mail, EmailMessage

# Create your views here.

class RegistrationView(CreateView):
	model = Registration
	success_url = reverse_lazy('marketing_register')
	template_name = 'marketing/register.html'
	form_class = RegistrationForm

	def send_event_mail(self, registration):
		print(registration.code)
		c = {
				"registration":registration
			}
		subject_template_name='email/event_registration_subject.txt'
		email_template_name='email/event_registrations_body.html'
		subject = loader.render_to_string(subject_template_name, c)
		# Email subject *must not* contain newlines
		subject = ''.join(subject.splitlines())
		email = loader.render_to_string(email_template_name, c)
		print("asdfasfdasfd")
		send_mail(subject, email, "bmsitutsaha2018@gmail.com" , [registration.email,], fail_silently=False,
			html_message=email)
		phone1 = registration.phone_no
		message = 'Hey, ' + registration.name + '. You\'ve registered for ' + registration.event.name + '. Your registration code is ' + registration.code + '. Venue : ' + registration.event.venue + ' Time : ' + str(registration.event.time) + ' You can also scan the QR Code sent to your email while attending the event. Enjoy!'
		params = { 'number' : phone1, 'text' : message }
		baseUrl = 'https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=62sxGWT6MkCjDul6eNKejw&senderid=BMSITM&channel=2&DCS=0&flashsms=0&' + ap.urlencode(params)
		urllib.request.urlopen(baseUrl).read(1000)
		messages.success(self.request, 'Registered Successfully!')

	def form_valid(self, form):
		form.instance.agent = self.request.user
		registration = form.save()

		registration.code = registration.gen_code()
		registration.save()

		self.send_event_mail(registration)

		return HttpResponseRedirect(self.success_url)


# def send_event_mail(request, registration_pk):
# 	registration = Registration.objects.get(pk=registration_pk)
# 	c = {
# 			"registration":registration
# 			}
# 	subject_template_name='email/event_registration_subject.txt'
# 	email_template_name='email/event_registrations_body.html'
# 	subject = loader.render_to_string(subject_template_name, c)
# 	# Email subject *must not* contain newlines
# 	subject = ''.join(subject.splitlines())
# 	email = loader.render_to_string(email_template_name, c)
# 	print("asdfasfdasfd")
# 	send_mail(subject, email, "feedback@bmsit.in" , ['agrawala.1697@gmail.com',], fail_silently=False)

# 	return HttpResponseRedirect(reverse_lazy('marketing_register'))

class RegistraionListView(TemplateView):
	template_name = "marketing/registrations_list.html"

	def get_context_data(self, **kwargs):
		context = super(RegistraionListView, self).get_context_data(**kwargs)
		event = Event.objects.get(coordinator=self.request.user)
		reg_list = Registration.objects.filter(event=event)
		context = {'event': event, 'reg_list': reg_list}
		return context















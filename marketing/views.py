from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib import messages

from general.models import Registration
from .forms import RegistrationForm

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
		send_mail(subject, email, "feedback@bmsit.in" , ['agrawala.1697@gmail.com',], fail_silently=False,
			html_message=email)
		messages.success(self.request, 'Registered Successfully!')

	def form_valid(self, form):
		form.instance.agent = self.request.user
		registration = form.save()

		registration.code = registration.gen_code()
		registration.save()

		self.send_event_mail(registration)

		return HttpResponseRedirect(self.success_url)


def send_event_mail(request, registration_pk):
	registration = Registration.objects.get(pk=registration_pk)
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
	send_mail(subject, email, "feedback@bmsit.in" , ['agrawala.1697@gmail.com',], fail_silently=False)

	return HttpResponseRedirect(reverse_lazy('marketing_register'))
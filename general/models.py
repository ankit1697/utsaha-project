from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Department(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class User(AbstractUser):
	'''
	User: Holds details about the user.
	'''
	phone = models.CharField("Phone", max_length=15, null=True, blank=True)
	sem = models.IntegerField("Semester", null=True, blank=True)
	department = models.ForeignKey("Department", on_delete=models.CASCADE, null=True)
	amount = models.DecimalField(default=0.0, max_digits=50, decimal_places=2, null=True)


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Event(models.Model):
	'''
	Event Details
	'''
	name = models.CharField("Name", max_length=50)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	coordinator = models.ForeignKey("User")
	category = models.ForeignKey("Category")
	date = models.DateField()
	time = models.TimeField()
	venue = models.CharField(max_length=50)

	# max registrations per event and whether or not to enforce that
	max_count = models.PositiveIntegerField(help_text="Max no. of registrations in an event")
	is_enforced = models.BooleanField()

	def __str__(self):
		if self.is_enforced:
			return "%s (%s) - left(%s)"%(self.name, str(self.price), str(self.max_count))
		return "%s (%s)"%(self.name, str(self.price))


class Registration(models.Model):
	'''
	Details of person registering for an event
	'''
	event = models.ForeignKey("Event")
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone_no = models.CharField(max_length=10)
	college = models.CharField(max_length=50)

	CASH="cash"
	PAYTM = "paytm"

	PAYMENT_CHOICES = ((CASH, "CASH"), (PAYTM, "PAYTM"))
	payment = models.CharField(max_length=5, choices=PAYMENT_CHOICES)
	agent = models.ForeignKey("User")
	is_attended = models.BooleanField(default=False)
	code = models.CharField(max_length=15, null=True, blank=True)
	date_created = models.DateField(auto_now_add=True, null=True)

	def __str__(self):
		return self.code

	def gen_code(self):
		return "100" + str(self.pk)

	def save(self, *args, **kwargs):
		if not self.pk:
			if self.event.is_enforced:
				self.event.max_count -= 1
				self.event.save()
		super(Registration, self).save(*args, **kwargs)
		

# from django.db.models.signals import post_save
# from django.dispatch import receiver

@receiver(post_save, sender=Registration)
def gen_code(sender, instance, **kwargs):
	instance.agent.amount += instance.event.price
	instance.agent.save()


from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Finance(models.Model):
	payor = models.CharField(max_length=50)
	payee = models.CharField(max_length=50)
	reason = models.TextField()
	amount = models.DecimalField(max_digits=15, decimal_places=2)
	image = models.ImageField(upload_to="bills", null=True, blank=True)
	date = models.DateField()
	mode_of_payment = models.CharField(max_length=50)
	transaction_id = models.CharField(max_length=50, null=True, blank=True)
	income = models.BooleanField(default=True)

	def __str__(self):
		return "%s-%s"%(self.payor, self.payee)
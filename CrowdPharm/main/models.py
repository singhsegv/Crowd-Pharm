from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Medicine(models.Model):
	medicine_name = models.CharField(max_length = 200)
	expiry_date = models.DateField(null=True)
	batch_no = models.CharField(max_length = 100)
	medicine_id = models.IntegerField()
	quantity = models.IntegerField(default=0, validators=[MinValueValidator(10)])
	image = models.FileField(null=True, blank=True)

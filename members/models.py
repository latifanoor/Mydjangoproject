from django.db import models


class Members(models.Model):
	full_name = models.CharField(max_length=100)
	phone_number=models.IntegerField()
	national_id = models.IntegerField()
	email=models.CharField(max_length=20)
	biography=models.CharField(max_length=100)
	Gender=models.CharField(max_length=20)
	dob = models.DateTimeField('date of birth')
	location = models.CharField(max_length=50)

	def __str__(self):
		return self.full_name
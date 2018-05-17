from django.db import models

# Create your models here.
class Members(models.Model):
	full_name = models.CharField(max_length=100)
	national_id = models.IntegerField()
	occupation = models.CharField(max_length=50)
	dob = models.DateTimeField('date of birth')
	location = models.CharField(max_length=50)
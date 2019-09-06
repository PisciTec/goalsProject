from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.

class Post(models.Model):
	"""docstring for Post"""
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title	
class Goal(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	name = models.CharField(max_length = 300)
	amount = models.DecimalField(max_digits=10 ,decimal_places = 2)
	created_date = models.DateTimeField(default = timezone.now)
	estimated_date = models.DateTimeField(blank = True, null = True)
	def publish(self):
		self.created_date = timezone.now()
		self.save()
	def __str__(self):
		return self.name
class Start_Value(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	name = models.CharField(max_length = 300)
	amount = models.DecimalField(max_digits=10 ,decimal_places = 2)
	created_date = models.DateTimeField(default = timezone.now)
	def publish(self):
		self.created_date = timezone.now()
		self.save()
	def __str__(self):
		return self.name

from django.db import models
from django.views.generic.list import ListView


# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField(null=True, blank=True)
	post_date = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-post_date'] 


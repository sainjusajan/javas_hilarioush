from django.db import models
from django.utils import timezone


class Post(models.Model):
	''' News Model 
	'''
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=100)
	pubDate = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	# Represents the model 
	def __str__(self):
		return self.title


class Photo(models.Model):
	'''Gallary Model
	'''
	pubDate = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(max_length = 50)
	image = models.ImageField(upload_to='gallery')
	description = models.TextField()

	# def __str__(self):
	# 	pass



class File(models.Model):
	'''File Model
	'''
	pubDate = models.DateTimeField(default=timezone.now)
	doc = models.FileField(upload_to='files')
	title = models.CharField(max_length=50)
	description = models.TextField()

	# Represents the File Model
	def __str__(self):
		return self.title



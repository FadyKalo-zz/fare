from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
	name = models.CharField(max_length=200)
	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.name


class Diet(models.Model):
	name = models.CharField(max_length=200)
	properties = models.CharField(max_length=200)
	recipes = models.ManyToManyField(Recipe, through='DietsCombinations')
	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.name


class Ingredient(models.Model):
	name = models.CharField(max_length=200)
	quantity = models.CharField(max_length=200)
	recipe = models.ForeignKey(Recipe)
	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.name


class DietsCombinations(models.Model):
	recipe = models.ForeignKey(Recipe)
	diet = models.ForeignKey(Diet)
	creat_date = models.DateField('date the diet was created')
	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return "%s - %s" % (self.diet, self.recipe)


class DietsUser(models.Model):
	diet = models.ForeignKey(Diet)
	user = models.ForeignKey(User)
	start_date = models.DateField('date the user started the diet')
	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return "%s - %s" % (self.diet, self.user)


class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username

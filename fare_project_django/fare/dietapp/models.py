from django.db import models
from django.contrib.auth.models import User


class Diet(models.Model):
	diet_name = models.CharField(max_length=200)
	diet_parameters = models.CharField(max_length=200)
	diet_decription = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s" % (self.diet_name)

# USER PROFILE ( website_link, age, height, weight?, gender, allergy, avg_cooking_time)
class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	age = models.PositiveIntegerField()
	height = models.PositiveIntegerField()
	weight = models.PositiveIntegerField()
	# gender = models.BooleanField()
	GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	avg_cooking_time = models.PositiveIntegerField()
	current_diet=models.OneToOneField(Diet,null=True)

	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username


#(User_id, Recipe_id, is_liked, is_consumed)
class RecipeActivity(models.Model):
	user_id = models.ForeignKey(User)
	recipe_id = models.CharField(max_length=200)
	is_liked = models.BooleanField()
	is_consumed = models.BooleanField()

	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return "%s - %s" % (self.recipe_id, self.user_id)


# (activity_type_id, activity_name)
class ActivityType(models.Model):
	activity_type_id = models.CharField(max_length=200)
	activity_name = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s - %s" % (self.activity_type_id, self.activity_name)


# Activity of User on the daily meals
# Activity_event(User_id, Recipe_id, Type_id, date_created)
class ActivityEvent(models.Model):
	user_id = models.ForeignKey(User)
	recipe_id = models.CharField(max_length=200)
	type_id = models.ForeignKey(ActivityType)
	date_created = models.DateTimeField()

	def __unicode__(self):
		return "%s - %s - %s" % (self.user_id, self.recipe_id, self.date_created)

class DietUser(models.Model):
	user = models.ForeignKey(User)
	diet = models.ForeignKey(Diet)
	start_date = models.DateField('date the user started the diet')

	def __unicode__(self):
		return "%s - %s" % (self.user, self.diet)



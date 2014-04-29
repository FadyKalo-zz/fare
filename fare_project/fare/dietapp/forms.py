__author__ = 'fady'
from django import forms
from dietapp.models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter a username.")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")
	email = forms.CharField(help_text="Please enter your email.")

	class Meta:
		model = User
		fields = ['username', 'password', 'email', ]


class UserProfileForm(forms.ModelForm):
	GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

	# website = forms.URLField(help_text="Please enter your website.", required=False)
	# picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)
	age = forms.IntegerField(help_text="Select your age.", required=True)
	weight = forms.IntegerField(help_text="Select your weight.", required=True, min_value=0)
	height = forms.IntegerField(help_text="Select your height", required=True, min_value=0)
	gender = forms.ChoiceField(help_text="Select your gender", required=True, choices=GENDER_CHOICES)
	avg_cooking_time = forms.IntegerField(help_text="Select your Average Cooking Time.", required=True, min_value=0)

	class Meta:
		model = UserProfile
		fields = [
			'height',
			'age',
			'weight',
			'avg_cooking_time',
			'gender'
			# 'website',
			# 'picture'
		]
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import logout

from yummly import *
import json
import helpFunc as hf
# from helpFunc import fetch_meals, getRecipeInfo

# needed in the register() view
from dietapp.forms import UserForm, UserProfileForm

def recipe(request):
	recipe_id = request.GET.get('recipe_id', '')

	try:
		recipe_details = hf.get_full_recipe_info(recipe_id)
		# info = hf.getRecipeInfo(recipe_id)

		attributes_of_interest = ["PROCNT", "FAT_KCAL", "FAPU", "CHOCDF","ENERC_KJ"]
		nutrition_elements = recipe_details["nutritionEstimates"]
		images=recipe_details["images"]
		nutrition_arr,images_arr,attr_arr = [],[],[]

		for k,v in recipe_details["attributes"].items():
			attr_arr +=v


		for x,v in images[0].items():
			images_arr.append(v)
		# print images_arr

		for x in nutrition_elements:
			dic = {}
			if x["attribute"] in attributes_of_interest:
				dic["description"] = x["description"]
				dic["value"] = x["value"]
				unit = x["unit"]
				dic["unit"] = unit["abbreviation"]
				nutrition_arr.append(dic)

		context = {"name": recipe_details["name"],

		   "attributes": attr_arr,
		   "time": recipe_details["totalTime"],
		   "ingredients": recipe_details["ingredientLines"],
		   "flavors": recipe_details["flavors"].update(
			   (x, y * 100) for x, y in recipe_details["flavors"].items()),
		   "nutrition": nutrition_arr,
		   # passing just the first picture here, can be improved
		   "images":images_arr[0]
		}
		print context["attributes"]

	except Recipe.DoesNotExist:
		raise Http404

	return render(request, 'dietapp/recipe.html', context)


@login_required
def diets_v2(request):
	template = loader.get_template('dietapp/diets_v2.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))


@login_required
def recipes_v2(request):
	template = loader.get_template('dietapp/recipes_v2.html')
	diet=request.GET.get('diet','')
	context = RequestContext(request, {
		'diet':diet
	})
	return HttpResponse(template.render(context))


@login_required
def get_recipes(request, meal):
	"""
	view function where we have a second parameter ( i.e: breakfast, dinner, lunch) and we call the yummly Api.

	:param request:
	:param meal:
	:return:
	"""
	myDiet = request.GET.get('diet', '')
	mealList = hf.fetch_meals(meal, myDiet)
	return HttpResponse(json.dumps(mealList), content_type="application/json")


@login_required
def recipeInfo(request):
	recipe_id = request.GET.get('recipe_id', '')
	if recipe_id != '':
		# info is a list of 2 lists where the first list is Ingredients and the second is nutrition
		info = hf.getRecipeInfo(recipe_id)
	else:
		# handle errors
		info = {'error': 'Recipe Id field is required!'}
	return HttpResponse(json.dumps(info), content_type="application/json")


def register(request):
	fav_color = request.session["fav_color"]
	print fav_color
	# Like before, get the request's context.
	context = RequestContext(request)

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

			# Did the user provide a profile picture?
			# If so, we need to get it from the input form and put it in the UserProfile model.
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			# Now we save the UserProfile model instance.
			profile.save()

			# Update our variable to tell the template registration was successful.
			registered = True

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print user_form.errors, profile_form.errors

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	# Render the template depending on the context.
	return render_to_response('dietapp/register.html',
							  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)


def user_login(request):

	# Set a session value:
	request.session["fav_color"] = "blue"

	# Obtain the context for the user's request.
	context = RequestContext(request)

	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']

		# To see if the username/password combination is valid
		user = authenticate(username=username, password=password)

		# If we have a User object, the details are correct.
		if user is not None:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# Send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/dietapp/')
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your Dietapp account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")

	# The request is not a HTTP POST, so display the login form.
	else:
		# No context variables to pass to the template system
		return render_to_response('dietapp/login.html', {}, context)


@login_required
def user_logout(request):
	# just log  out.
	logout(request)

	# Take the user back to the homepage.
	return HttpResponseRedirect('/dietapp/')

@login_required
def settings_page(request):
	template = loader.get_template('dietapp/settings_page.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))
from django.shortcuts import render
from yummly import *
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from dietapp.models import Recipe, Diet
import json
from helpFunc import fetch_meals

# here I import the json library. NOTE : Add it on the server ???

# def index(request):
#     # Obtain the context from the HTTP request.
#     context = RequestContext(request)
#
#     # Query the database for a list of ALL categories currently stored.
#     # Order the categories by no. likes in descending order.
#     # Retrieve the top 5 only - or all if less than 5.
#     # Place the list in our context_dict dictionary which will be passed to the template engine.
#     category_list = Recipe.objects.order_by('-likes')[:5]
#     context_dict = {'categories': category_list}
#
#     # Render the response and send it back!
#     return render_to_response('rango/index.html', context_dict, context)


# def recipe(request):
# 	recipe_list = Recipe.objects.order_by('name')[:5]
# 	output = recipe_list
# 	# output = ', '.join([p.ingredient_set.all() for p in recipe_list])
# 	return HttpResponse(output)

def recipes(request):
	recipe_list = Recipe.objects.order_by('name')[:5]
	template = 'dietapp/recipes.html'
	context = {
	'recipe_list': recipe_list,
	}
	return render(request, template, context)


def recipe(request, recipe_id):
	try:
		recipe = Recipe.objects.get(pk=recipe_id)
	except Recipe.DoesNotExist:
		raise Http404
	return render(request, 'dietapp/recipe.html', {'recipe': recipe})


def diets(request):
	diet_list = Diet.objects.order_by('name')[:5]
	template = loader.get_template('dietapp/diets.html')
	context = RequestContext(request, {
	'diet_list': diet_list,
	})
	return HttpResponse(template.render(context))


def diet(request, diet_id):
	try:
		diet = Diet.objects.get(pk=diet_id)
	except Recipe.DoesNotExist:
		raise Http404
	return render(request, 'dietapp/diet.html', {'diet': diet})

# get_recipes --> view function where we have a second parameter ( i.e: breakfast, dinner, lunch) and we call the yummly Api.
def get_recipes(request, meal):
	mealList = fetch_meals(meal)
	return HttpResponse(json.dumps(mealList), content_type="application/json")


def diets_v2(request):
	diet_list = Diet.objects.order_by('name')[:5]
	template = loader.get_template('dietapp/diets_v2.html')
	context = RequestContext(request, {
	'diet_list': diet_list,
	})
	return HttpResponse(template.render(context))


def recipes_v2(request):
	diet_list = Diet.objects.order_by('name')[:5]
	template = loader.get_template('dietapp/recipes_v2.html')
	context = RequestContext(request, {
	'diet_list': diet_list,
	})
	return HttpResponse(template.render(context))


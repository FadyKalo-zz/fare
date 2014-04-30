import yummly as ym
import json
import diet_settings as ds
from dietapp.models import Diet

#TODO(fady): this one has to become a secrets.json
TIMEOUT = 5.0
RETRIES = 0
API_ID = 'f679e06d'
API_KEY = 'b7d0fb2f961db4832b468523283d5bc0'
# connect to the API
client = ym.Client(api_id=API_ID, api_key=API_KEY, timeout=TIMEOUT, retries=RETRIES)


def blend(diet, user, adjustment, meal):
	temp_dict = {}
	for current in [diet, user, adjustment]:
		for k, v in current.items():
			if k in temp_dict:
				if isinstance(v, list):
					temp_dict[k] += v
				else:
					temp_dict[k] = v
			else:
				temp_dict[k] = v
	temp_dict["allowedCourse[]"] = ds.params_course[meal]
	return temp_dict


def get_meals(meal_type, diet):
	"""

	:rtype : object
	:param meal_type:
	:param diet:
	:return:
	"""

	a = Diet.objects.get(diet_name=diet).diet_parameters
	myjson = json.loads(a)

	diet_param = myjson
	user_param = {}
	adjust_param = {}
	final_params = blend(diet_param, user_param, adjust_param, meal_type)
	# if meal_type in "breakfast":
	# 	print final_params

	# execute the search with the selected list of parameters
	results = client.search(**final_params)

	# dictionary for storing the results from the yummly api.
	meals = {}
	# associate the image url and recipe id with the recipe name
	for match in results.matches:
		meals[match.recipeName] = [match.smallImageUrls, match.id, match.totalTimeInSeconds, match.rating,
			match.attributes]

	return meals


def insert_param(meal_type, diet, specifics, param_dict):
	"""

	given a diet e.g: 'Veggie' as a parameter and the Specifics of each diet this
	function adds the dietSpecific parameter to the generic ones. i.e: StdParams -- enterFunc --

	:rtype : dict
	:param meal_type:
	:param diet:
	:param specifics:
	:param param_dict:
	:return:
	"""
	param_dict['q'] = meal_type
	for key, value in specifics.items():
		if key == diet:
			param_dict.update({value[0]: value[1]})
	return param_dict


def get_recipe_info(recipe_id):
	"""

	:rtype : list
	:param recipe_id:
	:return:
	"""

	# the recipe function returns a recipe object
	recipeInfo = client.recipe(recipe_id)
	# get the IngredientLines attribute (a list) from the recipe object
	ingredients = recipeInfo.ingredientLines
	# get the nutritionEstimates attibute ( a list)
	nutrition = recipeInfo.nutritionEstimates
	infos = [ingredients, nutrition]

	return infos


def get_recipe(recipe_id):
	"""

	:rtype : dict
	:param recipe_id:
	:return:
	"""

	# the recipe function returns a recipe object
	recipe_info = client.recipe(recipe_id)
	return recipe_info


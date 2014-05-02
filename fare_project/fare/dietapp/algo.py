import yummly as ym
import json
import diet_settings as ds
from dietapp.models import Diet
from fare.settings import get_secret

TIMEOUT = 5.0
RETRIES = 0
API_ID = get_secret("YUMMLY_API_ID")
API_KEY = get_secret("YUMMLY_API_KEY")
# connect to the API
client = ym.Client(api_id=API_ID, api_key=API_KEY, timeout=TIMEOUT, retries=RETRIES)


#TODO(fady): check for conflict in the blend of parameters
def blend(diet, user, adjustment, meal):
	"""

	:param diet:
	:param user:
	:param adjustment:
	:param meal:
	:return:
	"""
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
	temp_dict["allowedCourse[]"] = ds.params_course_allowed[meal]
	temp_dict["excludedCourse[]"] = ds.params_course_excluded[meal]
	return temp_dict


def get_meals(meal_type, diet):
	"""

	:rtype : object
	:param meal_type:
	:param diet:
	:return:
	"""

	diet_param = json.loads(Diet.objects.get(diet_name=diet).diet_parameters)
	user_param = {}
	adjust_param = {}
	final_params = blend(diet_param, user_param, adjust_param, meal_type)
	if meal_type in "dinner":
		print final_params

	# execute the search with the selected list of parameters
	results = client.search(**final_params)

	# dictionary for storing the results from the yummly api.
	meals = {}
	# associate the image url and recipe id with the recipe name
	for match in results.matches:
		meals[match.recipeName] = [match.smallImageUrls, match.id, match.totalTimeInSeconds, match.rating,
			match.attributes]

	return meals


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


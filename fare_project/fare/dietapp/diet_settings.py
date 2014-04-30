standards = ["breakfast", "lunch", "snack", "dinner"]

std_params = {
	"q": "breakfast", # make this generic
	"start": 0,
	"maxResult": 10,
	"requirePicutres": True,
	"maxTotalTimeInSeconds": 3600,
}

# A dictionary of diet particular parameters to be added to the call to the Yummly API call.
# Rules: if the variable key or Value is anything but integer represent as string. e.g allowedAllergy is a list make --> 'allowedAllergy'.
# Not optimal solution, but works for appending extra parameters to the above StdParams seamlessly.
diets_specifics = {
	"Veggie": ["flavor.meaty.max", 0],
	"ProteinHigh": ["nutrition.PROCNT.min", 20],
	"GlutenFreeDelicious": ["allowedAllergy[]", ["Gluten-Free"]]
}

params_course = {
	"breakfast": ["course^course-Breakfast and Brunch"],
	"lunch": ["course^course-Main Dishes", "course^course-Lunch and Snacks"],
	"snack": ["course^course-Lunch and Snacks"],
	"dinner": [""]
}

params_veggie = {
"q": "",
"start": 0,
"maxResult": 10,
"requirePicutres": True,
"facetField[]": ["ingredient", "diet"],
"allowedDiet[]": ["387^Lacto-ovo vegetarian"],
"maxTotalTimeInSeconds": 3600,
}

params_protein_high = {
"q": "",
"start": 0,
"maxResult": 10,
"requirePicutres": True,
"facetField[]": ["ingredient", "diet"],
"maxTotalTimeInSeconds": 3600,
"nutrition.PROCNT.min": 20
}

params_gluten_free = {
"q": "",
"start": 0,
"maxResult": 10,
"requirePicutres": True,
"facetField[]": ["ingredient", "diet"],
"maxTotalTimeInSeconds": 3600,
"allowedAllergy[]": "393^Gluten-Free",
}

params_000 = {
"q": "pork chops",
"start": 0,
"maxResult": 40,
"requirePicutres": True,
"facetField[]": ["ingredient", "diet"],

"allowedIngredient[]": ["salt", "pepper"],
"excludedIngredient[]": ["cumin", "paprika"],

"allowedAllergy[]": "",
"allowedDiet[]": "",
"allowedCuisine[]": "",
"excludedCuisine[]": "",
"allowedCourse[]": "",
"excludedCourse[]": "",
"allowedHoliday[]": "",
"excludedHoliday[]": "",

"maxTotalTimeInSeconds": 3600,

# "nutrition.ATTR_NAME.{min | max}": "",
# "flavor.{sweet|meaty|sour|bitter|sweet|piquant}.{min|max}": "",

}

params_999 = {
"q": "pork chops",
"start": 0,
"maxResult": 40,
"requirePicutres": True,
"facetField[]": ["ingredient", "diet"],

"allowedIngredient[]": ["salt", "pepper"],
"excludedIngredient[]": ["cumin", "paprika"],

"allowedAllergy[]": "",
"allowedDiet[]": "",
"allowedCuisine[]": "",
"excludedCuisine[]": "",
"allowedCourse[]": "",
"excludedCourse[]": "",
"allowedHoliday[]": "",
"excludedHoliday[]": "",

"maxTotalTimeInSeconds": 3600,
"flavor.meaty.min": 0.5,
"flavor.meaty.max": 1,
"flavor.sweet.min": 0,
"flavor.sweet.max": 0.5,
"nutrition.FAT.min": 0,
"nutrition.FAT.max": 15

# "nutrition.ATTR_NAME.{min | max}": "",
# "flavor.{sweet|meaty|sour|bitter|sweet|piquant}.{min|max}": "",

}

json_course = {"course": [
	{"id": "course-Main Dishes", "name": "Main Dishes", "type": "course", "description": "Main Dishes",
	"searchValue": "course^course-Main Dishes", "localesAvailableIn": ["en-US"]},
	{"id": "course-Desserts", "name": "Desserts", "type": "course", "description": "Desserts",
	"searchValue": "course^course-Desserts", "localesAvailableIn": ["en-US"]},
	{"id": "course-Side Dishes", "name": "Side Dishes", "type": "course", "description": "Side Dishes",
	"searchValue": "course^course-Side Dishes", "localesAvailableIn": ["en-US"]},
	{"id": "course-Lunch and Snacks", "name": "Lunch and Snacks", "type": "course", "description": "Lunch and Snacks",
	"searchValue": "course^course-Lunch and Snacks", "localesAvailableIn": ["en-US"]},
	{"id": "course-Appetizers", "name": "Appetizers", "type": "course", "description": "Appetizers",
	"searchValue": "course^course-Appetizers", "localesAvailableIn": ["en-US"]},
	{"id": "course-Salads", "name": "Salads", "type": "course", "description": "Salads",
	"searchValue": "course^course-Salads", "localesAvailableIn": ["en-US"]},
	{"id": "course-Breakfast and Brunch", "name": "Breakfast and Brunch", "type": "course",
	"description": "Breakfast and Brunch", "searchValue": "course^course-Breakfast and Brunch",
	"localesAvailableIn": ["en-US"]},
	{"id": "course-Breads", "name": "Breads", "type": "course", "description": "Breads",
	"searchValue": "course^course-Breads", "localesAvailableIn": ["en-US"]},
	{"id": "course-Soups", "name": "Soups", "type": "course", "description": "Soups",
	"searchValue": "course^course-Soups", "localesAvailableIn": ["en-US"]},
	{"id": "course-Beverages", "name": "Beverages", "type": "course", "description": "Beverages",
	"searchValue": "course^course-Beverages", "localesAvailableIn": ["en-US"]},
	{"id": "course-Condiments and Sauces", "name": "Condiments and Sauces", "type": "course",
	"description": "Condiments and Sauces", "searchValue": "course^course-Condiments and Sauces",
	"localesAvailableIn": ["en-US"]},
	{"id": "course-Cocktails", "name": "Cocktails", "type": "course", "description": "Cocktails",
	"searchValue": "course^course-Cocktails", "localesAvailableIn": ["en-US"]}]}

json_diet = {"diet": [
	{"id": "386", "shortDescription": "Vegan", "longDescription": "Vegan", "searchValue": "386^Vegan", "type": "diet",
	"localesAvailableIn": ["en-US", "en-GB"]},
	{"id": "388", "shortDescription": "Lacto vegetarian", "longDescription": "Lacto vegetarian",
	"searchValue": "388^Lacto vegetarian", "type": "diet", "localesAvailableIn": ["en-US", "en-GB"]},
	{"id": "389", "shortDescription": "Ovo vegetarian", "longDescription": "Ovo vegetarian",
	"searchValue": "389^Ovo vegetarian", "type": "diet", "localesAvailableIn": ["en-US", "en-GB"]},
	{"id": "390", "shortDescription": "Pescetarian", "longDescription": "Pescetarian", "searchValue": "390^Pescetarian",
	"type": "diet", "localesAvailableIn": ["en-US", "en-GB"]},
	{"id": "387", "shortDescription": "Lacto-ovo vegetarian", "longDescription": "Vegetarian",
	"searchValue": "387^Lacto-ovo vegetarian", "type": "diet", "localesAvailableIn": ["en-US", "en-GB"]}]}
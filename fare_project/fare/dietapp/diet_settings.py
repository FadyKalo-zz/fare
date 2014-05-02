params_std = {
"q": "", # make this generic
"start": 0,
"maxResult": 10,
"requirePicutres": True,
"maxTotalTimeInSeconds": 3600,
}

params_course_allowed = {
"breakfast": ["course^course-Breakfast and Brunch"],
"lunch": ["course^course-Main Dishes", "course^course-Lunch and Snacks"],
"snack": ["course^course-Lunch and Snacks", "course^course-Desserts"],
"dinner": []
}

params_course_excluded = {
"breakfast": ["course^course-Cocktails", "course^course-Condiments and Sauces", "course^course-Beverages"],
"lunch": ["course^course-Cocktails", "course^course-Condiments and Sauces", "course^course-Beverages"],
"snack": ["course^course-Cocktails", "course^course-Condiments and Sauces", "course^course-Beverages"],
"dinner": ["course^course-Cocktails", "course^course-Condiments and Sauces", "course^course-Beverages",
	"course^course-Desserts", "course^course-Breads"]
}

params_veggie = {
	"facetField[]": ["ingredient", "diet"],
	"allowedDiet[]": ["387^Lacto-ovo vegetarian"],
}

params_protein_high = {
	"facetField[]": ["ingredient", "diet"],
	"nutrition.PROCNT.min": 20
}

params_gluten_free = {
	"facetField[]": ["ingredient", "diet"],
	"allowedAllergy[]": "393^Gluten-Free",
}
params_italian = {
	"allowedCuisine[]": "cuisine^cuisine-italian",
}
params_greek = {
	"allowedCuisine[]": "cuisine^cuisine-greek",
}

params_mexican = {
	"allowedCuisine[]": "cuisine^cuisine-mexican",
}

params_japanese = {
	"allowedCuisine[]": "cuisine^cuisine-japanese",
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

json_cuisine = {'cuisine': [
	{"id": "cuisine-american", "name": "American", "type": "cuisine", "description": "American",
	"searchValue": "cuisine^cuisine-american", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-italian", "name": "Italian", "type": "cuisine", "description": "Italian",
	"searchValue": "cuisine^cuisine-italian", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-asian", "name": "Asian", "type": "cuisine", "description": "Asian",
	"searchValue": "cuisine^cuisine-asian", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-mexican", "name": "Mexican", "type": "cuisine", "description": "Mexican",
	"searchValue": "cuisine^cuisine-mexican", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-southern", "name": "Southern & Soul Food", "type": "cuisine", "description": "Southern & Soul Food",
	"searchValue": "cuisine^cuisine-southern", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-french", "name": "French", "type": "cuisine", "description": "French",
	"searchValue": "cuisine^cuisine-french", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-southwestern", "name": "Southwestern", "type": "cuisine", "description": "Southwestern",
	"searchValue": "cuisine^cuisine-southwestern", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-barbecue-bbq", "name": "Barbecue", "type": "cuisine", "description": "Barbecue",
	"searchValue": "cuisine^cuisine-barbecue-bbq", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-indian", "name": "Indian", "type": "cuisine", "description": "Indian",
	"searchValue": "cuisine^cuisine-indian", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-chinese", "name": "Chinese", "type": "cuisine", "description": "Chinese",
	"searchValue": "cuisine^cuisine-chinese", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-cajun", "name": "Cajun & Creole", "type": "cuisine", "description": "Cajun & Creole",
	"searchValue": "cuisine^cuisine-cajun", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-mediterranean", "name": "Mediterranean", "type": "cuisine", "description": "Mediterranean",
	"searchValue": "cuisine^cuisine-mediterranean", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-greek", "name": "Greek", "type": "cuisine", "description": "Greek",
	"searchValue": "cuisine^cuisine-greek", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-english", "name": "English", "type": "cuisine", "description": "English",
	"searchValue": "cuisine^cuisine-english", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-spanish", "name": "Spanish", "type": "cuisine", "description": "Spanish",
	"searchValue": "cuisine^cuisine-spanish", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-thai", "name": "Thai", "type": "cuisine", "description": "Thai",
	"searchValue": "cuisine^cuisine-thai", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-german", "name": "German", "type": "cuisine", "description": "German",
	"searchValue": "cuisine^cuisine-german", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-moroccan", "name": "Moroccan", "type": "cuisine", "description": "Moroccan",
	"searchValue": "cuisine^cuisine-moroccan", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-irish", "name": "Irish", "type": "cuisine", "description": "Irish",
	"searchValue": "cuisine^cuisine-irish", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-japanese", "name": "Japanese", "type": "cuisine", "description": "Japanese",
	"searchValue": "cuisine^cuisine-japanese", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-cuban", "name": "Cuban", "type": "cuisine", "description": "Cuban",
	"searchValue": "cuisine^cuisine-cuban", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-hawaiian", "name": "Hawaiian", "type": "cuisine", "description": "Hawaiian",
	"searchValue": "cuisine^cuisine-hawaiian", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-swedish", "name": "Swedish", "type": "cuisine", "description": "Swedish",
	"searchValue": "cuisine^cuisine-swedish", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-hungarian", "name": "Hungarian", "type": "cuisine", "description": "Hungarian",
	"searchValue": "cuisine^cuisine-hungarian", "localesAvailableIn": ["en-US"]},
	{"id": "cuisine-portuguese", "name": "Portuguese", "type": "cuisine", "description": "Portuguese",
	"searchValue": "cuisine^cuisine-portuguese", "localesAvailableIn": ["en-US"]}]}

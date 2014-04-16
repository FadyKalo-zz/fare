standards = ['breakfast', 'lunch', 'snack', 'dinner']

StdParams = {
	'q': 'breakfast', # make this generic
	'start': 0,
	'maxResult': 10,
	'requirePicutres': True,
	'maxTotalTimeInSeconds': 3600,
}

# A dictionary of diet particular parameters to be added to the call to the Yummly API call.
# Rules: if the variable key or Value is anything but integer represent as string. e.g allowedAllergy is a list make --> 'allowedAlergy'.
# Not optimal solution, but works for appending extra parameters to the above StdParams seamlessly.
DietsSpecifics = {
	'Veggie': ['flavor.meaty.max', 0],
	'ProteinHigh': ['nutrition.PROCNT.min', 20],
	'GlutenFreeDelicious': ['allowedAllergy[]', ['Gluten-Free']]
}

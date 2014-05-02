__author__ = 'fady'
import diet_settings as ds
import os, sys, json


def add_diet(name, title, params, description):
	d = Diet.objects.get_or_create(diet_name=name, diet_title=title, diet_parameters=json.dumps(params),
		diet_description=description)[0]
	return d


def populate():
	"""

	"""

	veggie_diet = ds.params_veggie
	veggie_diet.update(ds.params_std)
	vd = add_diet("veggie", "Veggie", veggie_diet, "Basic vegeterian diet")

	protein_diet = ds.params_protein_high
	protein_diet.update(ds.params_std)
	pd = add_diet("protein_high", "Protein High", protein_diet, "Let's add some protein")

	gluten_free_diet = ds.params_gluten_free
	gluten_free_diet.update(ds.params_std)
	gd = add_diet("gluten_free", "Gluten Free", gluten_free_diet, "No starch today")

	italian_diet = ds.params_italian
	italian_diet.update(ds.params_std)
	itd = add_diet("italian", "Italian", italian_diet, "Your palate says thanks")

	greek_diet = ds.params_greek
	greek_diet.update(ds.params_std)
	gkd = add_diet("greek", "Greek", greek_diet, "The real deal")

	mexican_diet = ds.params_mexican
	mexican_diet.update(ds.params_std)
	med = add_diet("mexican", "Mexican", mexican_diet, "Spice up your meal")

	japanese_diet = ds.params_japanese
	japanese_diet.update(ds.params_std)
	jpd = add_diet("japanese", "Japanese", japanese_diet, "Sophisticate your diet")


# a = Diet.objects.get(diet_name="test").diet_parameters
# to_convert = a
# print type(to_convert)
# myjson = json.loads(to_convert)

if __name__ == '__main__':
	script_path = os.path.dirname(__file__)
	project_dir = os.path.abspath(os.path.join(script_path, '..', '..', 'fare'))
	sys.path.insert(0, project_dir)
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fare.settings')
	from dietapp.models import Diet

	populate()

__author__ = 'fady'
import diet_settings as ds
import os, sys, json


def add_diet(name, title, params, description):
	d = Diet.objects.get_or_create(diet_name=name, diet_title=title,diet_parameters=json.dumps(params), diet_description=description)[0]
	return d


def populate():
	"""

	"""

	veggie_diet = ds.params_veggie
	vd = add_diet("veggie","Veggie" ,veggie_diet, "basic vegeterian diet")

	protein_diet = ds.params_protein_high
	pd = add_diet("protein_high", "Protein High",protein_diet, "let's add some protein")

	gluten_free_diet = ds.params_gluten_free
	gd = add_diet("gluten_free","Gluten Free" ,gluten_free_diet, "no starch today")


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

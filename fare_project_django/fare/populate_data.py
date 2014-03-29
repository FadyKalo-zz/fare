# -*- coding: utf-8 -*-

__author__ = 'fady'

import os
from datetime import date


def populate():
	# create recipes
	margherita = add_recipe('pizza')
	bruschetta = add_recipe('bruschetta')
	pasta_al_ragu = add_recipe('pasta al ragù')
	ribs = add_recipe('ribs')
	burger = add_recipe('burger')
	penne_al_pesto = add_recipe('penne al pesto')
	spaghetti_carbonara = add_recipe('spaghetti alla carbonara')

	# create ingredients
	# margherita
	marg_1 = add_ingredient('tomato', 'some', margherita)
	marg_2 = add_ingredient('mozzarella', 'some', margherita)
	marg_3 = add_ingredient('dough', 'some', margherita)

	# bruschetta
	brus_1 = add_ingredient('bread', 'some', bruschetta)
	brus_2 = add_ingredient('garlic', 'a lot', bruschetta)
	brus_3 = add_ingredient('tomato', 'some', bruschetta)

	# pasta al ragu
	ragu_1 = add_ingredient('pasta', 'some', pasta_al_ragu)
	ragu_2 = add_ingredient('tomato', 'some', pasta_al_ragu)
	ragu_3 = add_ingredient('meat', 'some', pasta_al_ragu)
	# spaghetti alla carbonara
	ragu_3 = add_ingredient('pasta', 'some', spaghetti_carbonara)
	ragu_3 = add_ingredient('carbonara', 'some', spaghetti_carbonara)
	ragu_3 = add_ingredient('eggs', 'some', spaghetti_carbonara)
	ragu_3 = add_ingredient('pecorino', 'some', spaghetti_carbonara)
	# pasta al pesto
	ragu_3 = add_ingredient('pasta', 'some', penne_al_pesto)
	ragu_3 = add_ingredient('pesto', 'some', penne_al_pesto)
	ragu_3 = add_ingredient('parmiagiano', 'a lot', penne_al_pesto)

	# ribs
	rib_1 = add_ingredient('ribs', 'rack', ribs)
	rib_2 = add_ingredient('bbq sauce', 'some', ribs)
	rib_3 = add_ingredient('potatoes', 'some', ribs)

	# burger
	burg_1 = add_ingredient('burger', 'some', burger)
	burg_1 = add_ingredient('bun', 'some', burger)
	burg_1 = add_ingredient('fries', 'some', burger)

	# create a diet
	mediterranean = add_diet("mediterranean")
	american = add_diet('american')
	only_pasta = add_diet('only pasta')

	# add the recipes to the diets
	add_diet_combinations(margherita, mediterranean)
	add_diet_combinations(bruschetta, mediterranean)
	add_diet_combinations(pasta_al_ragu, mediterranean)

	add_diet_combinations(burger, american)
	add_diet_combinations(ribs, american)
	add_diet_combinations(margherita, american)

	add_diet_combinations(pasta_al_ragu,only_pasta)
	add_diet_combinations(spaghetti_carbonara,only_pasta)
	add_diet_combinations(penne_al_pesto,only_pasta)


def printlog():
# Print out what we have added to the user.
	for r in Recipe.objects.all():
		for i in Ingredient.objects.filter(recipe=r):
			print "- {0} - {1}".format(str(r), str(i))

	for d in Diet.objects.all():
		for r in d.recipes.all():
			print "- {0} - {1}".format(str(d), str(r))


# def add_page(cat, title, url, views=0):
# 	p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
# 	return p
#
#
# def add_cat(name):
# 	c = Category.objects.get_or_create(name=name)[0]
# 	return c


def add_ingredient(name, quantity, recipe):
	i = Ingredient.objects.get_or_create(name=name, quantity=quantity, recipe=recipe)[0]
	return i


def add_recipe(name):
	r = Recipe.objects.get_or_create(name=name)[0]
	return r


def add_diet(name):
	d = Diet.objects.get_or_create(name=name)[0]
	return d


def add_diet_combinations(recipe, diet):
	dc = DietsCombinations.objects.get_or_create(recipe=recipe, diet=diet, creat_date=date.today())[0]
	# m1.save()
	return dc

# Start execution here!

if __name__ == '__main__':
	print "Starting FARE population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fare.settings')
	from dietapp.models import Ingredient, Recipe, Diet, DietsCombinations, DietsUser

	populate()
	printlog()
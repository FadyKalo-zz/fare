__author__ = 'fady'

from django.conf.urls import patterns, url
from dietapp import views

urlpatterns = patterns('',

    url(r'^diets/', views.diets, name='diets'),
	url(r'^diet/(?P<diet_id>\d+)/$', views.diet, name='diet'),

    url(r'^recipes/', views.recipes, name='recipes'),
	url(r'^recipe/(?P<recipe_id>\d+)/$', views.recipe, name='recipe'),
    url(r'^recipe/(?P<meal>\w{5,10})/$', views.get_recipes, name = 'get_recipes'),
    url(r'^$', views.diets_v2, name = 'home'),
	url(r'^meals/$', views.recipes_v2, name = 'meals'),

)
__author__ = 'fady'

from django.conf.urls import patterns, url
from dietapp import views

urlpatterns = patterns('',
					   url(r'^recipe/(?P<meal>\w{5,10})/$', views.get_recipes, name='get_recipes'),
					   url(r'^$', views.diets_v2, name='home'),
					   url(r'^settings/$', views.settings_page, name='settings'),
					   url(r'^meals/$', views.recipes_v2, name='meals'),
					   url(r'^meals/(?P<diet>\w+)/$', views.get_recipes, name='get_recipes'),
					   url(r'^recipe/$', views.recipe, name='recipe'),
					   # call this url http://127.0.0.1:8080/dietapp/diet/meal/recipe/?recipe_id=Pomegranate-Breakfast-Soda-Food-Network
					   url(r'^register/$', views.register, name='register'), # ADDED NEW PATTERN FOR THE REGISTRATION!
					   url(r'^login/$', views.user_login, name='login'), # ADDED NEW PATTERN FOR THE LOGIN!
					   url(r'^logout/$', views.user_logout, name='logout'), # ADDED NEW PATTERN FOR THE LOGOUT!
)



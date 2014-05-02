__author__ = 'fady'

from django.conf.urls import patterns, url
from dietapp import views

urlpatterns = patterns('',
	url(r'^recipe/(?P<meal>\w{5,10})/$', views.get_recipes, name='get_recipes'),
	url(r'^recipe/like/(?P<rec_id>\w+(?:-\w+)+)/$', views.recipe_like, name='recipe_like'),
	url(r'^recipe/eaten/(?P<rec_id>\w+(?:-\w+)+)/$', views.recipe_eaten, name='recipe_eaten'),
	# url(r'^$', views.diets, name='home'),
	url(r'^$', views.diets, name='home'),
	url(r'^settings/$', views.settings_page, name='settings'),
	url(r'^meals/$', views.daily_meals, name='meals'),
	# url(r'^meals/(?P<diet>\w+)/$', views.get_recipes, name='get_recipes'),
	url(r'^recipe/$', views.recipe, name='recipe'),
	url(r'^register/$', views.register, name='register'), # ADDED NEW PATTERN FOR THE REGISTRATION!
	url(r'^login/$', views.user_login, name='login'), # ADDED NEW PATTERN FOR THE LOGIN!
	url(r'^logout/$', views.user_logout, name='logout'), # ADDED NEW PATTERN FOR THE LOGOUT!
)
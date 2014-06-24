from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from django.utils import timezone
import json
import datetime as dt
import algo as alg

# needed in the register() view
from dietapp.forms import UserForm, UserProfileForm
from models import UserProfile, Diet, DietUser, UserDailyMeals, ActivityEvent, ActivityType, RecipeActivity


def recipe(request):
    recipe_id = request.GET.get('recipe_id', '')
    pk_user = request.user

    try:
        recipe_details = alg.get_recipe(recipe_id)
        # info = hf.getRecipeInfo(recipe_id)

        attributes_of_interest = ["PROCNT", "FAT_KCAL", "FAPU", "CHOCDF", "ENERC_KJ"]
        nutrition_elements = recipe_details["nutritionEstimates"]
        images = recipe_details["images"]
        nutrition_arr, images_arr, attr_arr = [], [], []

        for k, v in recipe_details["attributes"].items():
            attr_arr += v

        for x, v in images[0].items():
            images_arr.append(v)

        recipe_details["flavors"].update((x, y * 100) for x, y in recipe_details["flavors"].items())

        for x in nutrition_elements:
            dic = {}
            if x["attribute"] in attributes_of_interest:
                dic["description"] = x["description"]
                dic["value"] = x["value"]
                unit = x["unit"]
                dic["unit"] = unit["abbreviation"]
                nutrition_arr.append(dic)

        context = {
        'id': recipe_id,
        'name': recipe_details["name"],
        'attributes': attr_arr,
        'time': recipe_details["totalTime"],
        'ingredients': recipe_details["ingredientLines"],
        'flavors': recipe_details["flavors"],
        'nutrition': nutrition_arr,
        'images': images_arr[0],
        # 'is_liked':False,
        # 'is_consumed':False
        }

        #TODO(fady): make this check for existence more efficient
        if RecipeActivity.objects.filter(user_id=pk_user, recipe_id=recipe_id).exists():
            recipe_activity = RecipeActivity.objects.get(user_id=pk_user, recipe_id=recipe_id)
            context['is_liked'] = recipe_activity.is_liked
            context['is_consumed'] = recipe_activity.is_consumed
            print context['is_liked'], context['is_consumed']
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'dietapp/recipe.html', context)


@login_required
def diets(request):
    template = 'dietapp/diets.html'
    available_diets = Diet.objects.all()
    context = {"diets": available_diets}
    return render(request, template, context)


@login_required
def daily_meals(request):
    template = loader.get_template('dietapp/daily_meals.html')
    diet = request.GET.get('diet', '')
    pk_user = request.user
    user_profile = UserProfile.objects.get(user=pk_user)
    current_diet = Diet.objects.get(diet_name=diet)

    now = timezone.now()
    obj, created = UserDailyMeals.objects.get_or_create(user=pk_user, defaults={'date': now})
    # check if the
    # previous = dt.datetime.now() - dt.timedelta(hours=100)
    previous = obj.date
    delta = (now - previous)
    print now
    print previous
    print obj
    flag = False
    #if it's a new day or the user changed the diet
    if delta.days > 0 or current_diet != diet:
        flag = True
        dic = {"breakfast": [], "lunch": [], "snack": [], "dinner": []}
        for k, v in dic.items():
            raw = alg.get_meals(k, diet)
            dic[k] = raw
        obj.meals = dic

    obj.date = now
    obj.save()
    # request.session["current_diet"] = diet
    # cur_diet = request.session["current_diet"]
    # print cur_diet

    # cur_diet = user_profile.current_diet
    # if cur_diet is None:
    user_profile.current_diet = current_diet
    diet_user = DietUser(user=pk_user, diet=current_diet, start_date=now)
    # print cur_diet, user_profile
    user_profile.save()
    diet_user.save()

    # print UserProfile.objects.get(user=pk_user).current_diet
    context = RequestContext(request, {'diet': diet, 'flag': flag})
    return HttpResponse(template.render(context))


@login_required
def get_recipes(request, meal):
    """
    view function where we have a second parameter ( i.e: breakfast, dinner, lunch) and we call the yummly Api.

    :param request:
    :param meal:
    :return:
    """

    diet = request.GET.get('diet', '')
    flag = request.GET.get('flag', '')
    #TODO(fady): use flag to determine which recipes to send back
    mealList = alg.get_meals(meal, diet)
    return HttpResponse(json.dumps(mealList), content_type="application/json")


@login_required
def recipe_like(request, rec_id):
    print 'in recipe_like'
    var = {}
    if request.method == 'GET':
        context = RequestContext(request)
        pk_user = request.user
        act_type = ActivityType.objects.get(activity_type_id="like")
        event = ActivityEvent(user_id=pk_user, recipe_id=rec_id, type_id=act_type, date_created=timezone.now())
        event.save()

        defaults = {'is_liked': True, 'is_consumed': False}
        obj, created = RecipeActivity.objects.get_or_create(user_id=pk_user, recipe_id=rec_id, defaults=defaults)
        if not created:
            obj.is_liked = True
        obj.save()
    #
    # cat_id = None
    # if request.method == 'GET':
    # 	cat_id = request.GET['category_id']
    #
    # likes = 0
    # if cat_id:
    # 	category = Category.objects.get(id=int(cat_id))
    # 	if category:
    # 		likes = category.likes + 1
    # 	category.likes = likes
    # 	category.save()
    #
    # return HttpResponse(likes)
    return HttpResponse(var, content_type="text")


@login_required
def recipe_eaten(request, rec_id):
    diet = request.GET.get('diet', '')
    return


@login_required
def recipeInfo(request):
    recipe_id = request.GET.get('recipe_id', '')
    if recipe_id != '':
        # info is a list of 2 lists where the first list is Ingredients and the second is nutrition
        info = alg.get_recipe_info(recipe_id)
    else:
        # handle errors
        info = {'error': 'Recipe Id field is required!'}
    return HttpResponse(json.dumps(info), content_type="application/json")


def register(request):
    fav_color = request.session["fav_color"]
    print fav_color
    # Like before, get the request context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response('dietapp/register.html',
                              {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
                              context)


def user_login(request):
    # Set a session value:
    request.session["fav_color"] = "blue"

    # Obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # To see if the username/password combination is valid
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # Send the user back to the homepage.
                login(request, user)
                cur_diet = None
                pk_user = request.user
                cur_diet = UserProfile.objects.get(user=pk_user).current_diet
                if cur_diet is not None:
                    ctx = {"diet": cur_diet}
                    # return render_to_response('dietapp/daily_meals.html', ctx, context_instance=RequestContext(request))
                    request.method = "GET"
                    request.GET = {"diet": cur_diet}
                    return daily_meals(request)
                else:
                    return HttpResponseRedirect(reverse('home'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Dietapp account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    else:
        # No context variables to pass to the template system
        return render_to_response('dietapp/login.html', {}, context)


@login_required
def user_logout(request):
    # just log  out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/dietapp/')


@login_required
def settings_page(request):
    context = RequestContext(request)
    user = request.user
    # username = None
    # if request.user.is_authenticated():
    # 	username = user.username

    this_profile = UserProfile.objects.get(user=user)
    # If it's a HTTP POST, we're interested in processing form data.
    registered = False
    if request.method == 'POST':

        profile_form = UserProfileForm(data=request.POST, instance=this_profile)

        # If the two forms are valid...
        if profile_form.is_valid():

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()
            # Update our variable to tell the template registration was successful.
            registered = True
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print profile_form.errors
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        profile_form = UserProfileForm(instance=this_profile)

    if registered:
        cur_diet = UserProfile.objects.get(user=user).current_diet
        ctx = {"diet": cur_diet}
        return render_to_response('dietapp/daily_meals.html', ctx, context_instance=RequestContext(request))
    else:
    # Render the template depending on the context.
        return render_to_response('dietapp/settings_page.html', {'profile_form': profile_form}, context)

        # print(username, user, user.email, user.get_username())
        # template = loader.get_template('dietapp/settings_page.html')
        # context = RequestContext(request, {})
        # return HttpResponse(template.render(context))
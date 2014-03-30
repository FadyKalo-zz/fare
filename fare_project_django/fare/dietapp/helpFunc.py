from yummly import *
from dataStandards import *

Diet = 'Veggie'


def fetch_meals(mealtype,Diet):
        TIMEOUT = 5.0
        RETRIES = 0

        # dictionary for storing the results from the yummly api.
        meals = {}
        # connect to the API
        client = Client(api_id='f679e06d', api_key='b7d0fb2f961db4832b468523283d5bc0', timeout=TIMEOUT, retries=RETRIES)

        # TODO: parameters = get_parameters(Diet)
        params = insertParam(mealtype, Diet, DietsSpecifics, StdParams)
        # execute the search with the selected list of parameters
        results = client.search(**params)
        # associate the image url and recipe id with the recipe name
        for match in results.matches:
            print match.smallImageUrls, match.id, match.totalTimeInSeconds, match.rating, match.attributes
            meals[match.recipeName] = [match.smallImageUrls, match.id, match.totalTimeInSeconds, match.rating, match.attributes]

        return meals

# given a diet e.g: 'Veggie' as a parameter and the Specifics of each diet this function adds the dietSpecific parameter to the generic ones
# i.e: StdParams -- enterFunc --
                             
def insertParam(mealType, diet, Specifics, aDict):
    #newDict = {}
    aDict['q'] = mealType
    for key,value in Specifics.items():
        if key == diet:
            aDict.update({value[0]:value[1]})
    return aDict


def getRecipeInfo(recipe_id):
    TIMEOUT = 5.0
    RETRIES = 0
    client = Client(api_id='f679e06d', api_key='b7d0fb2f961db4832b468523283d5bc0', timeout=TIMEOUT, retries=RETRIES)
    # the recipe function returns a recipe object
    recipeInfo=client.recipe(recipe_id) 

    # get the IngredientLines attribute (a list) from the recipe object
    ingredients=recipeInfo.ingredientLines

    # get the nutritionEstimates attibute ( a list) 
    nutrition=recipeInfo.nutritionEstimates
    
    infos=[ingredients,nutrition]

    return infos






def main():
    results1 = fetch_meals('breakfast', Diet)
    #getRecipeInfo('Pomegranate-Breakfast-Soda-Food-Network')



if __name__ == '__main__':
     main()

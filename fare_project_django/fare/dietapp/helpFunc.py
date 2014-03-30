from yummly import *
from dataStandards import *

Diet = 'Veggie'


def fetch_meals(mealtype,Diet):
        TIMEOUT = 5.0
        RETRIES = 0

        # dictionary for storing the results from the yummly api.
        meals = {}

        client = Client(api_id='f679e06d', api_key='b7d0fb2f961db4832b468523283d5bc0', timeout=TIMEOUT, retries=RETRIES)
        #search = client.search('breakfast') 
        #match = search.matches[0]
        # TODO: parameters = get_parameters(Diet)
        params = insertParam(mealtype, Diet, DietsSpecifics, StdParams)
        results = client.search(**params)
        for match in results.matches:
            print " match id: ", match.id
            meals[match.recipeName] = [match.smallImageUrls, match.id]
            #print "------------------------------"
            #print 'id is ', match.id"""
        return meals

# given a diet e.g: 'Veggie' as a parameter and the Specifics of each diet this function adds the dietSpecific parameter to the generic ones
# i.e: StdParams -- enterFunc --
                             
def insertParam(mealType, diet, Specifics, aDict):
    #newDict = {}
    aDict['q'] = mealType
    for key,value in Specifics.items():
        if key == diet:
            aDict.update({value[0]:value[1]})
            print "This is the " + diet +"'s parameters", aDict
    return aDict


def getRecipeInfo(recipe_id):
    TIMEOUT = 5.0
    RETRIES = 0
    client = Client(api_id='f679e06d', api_key='b7d0fb2f961db4832b468523283d5bc0', timeout=TIMEOUT, retries=RETRIES)
    recipeInfo=client.recipe(recipe_id)
    ingredients=recipeInfo.ingredientLines
    nutrition=recipeInfo.nutritionEstimates
    infos=[ingredients,nutrition]
    """print " nutrition facts: ", recipeInfo.nutritionEstimates
    for ingred in recipeInfo.ingredientLines:
        print ' ingredient: ', ingred
    """

    return infos






def main():
    #results1 = fetch_meals('breakfast', Diet)
    getRecipeInfo('Pomegranate-Breakfast-Soda-Food-Network')



if __name__ == '__main__':
     main()

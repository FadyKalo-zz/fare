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
            meals[match.recipeName] = match.smallImageUrls
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



# def main():
#     results1 = fetch_meals('breakfast', Diet)
#     for k in results1:
#         print k
#
#
# if __name__ == '__main__':
#     main()

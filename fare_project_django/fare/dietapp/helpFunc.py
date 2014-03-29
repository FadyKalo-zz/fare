from yummly import *


standards = ['breakfast','lunch', 'snack', 'dinner']


def fetch_meals(mealtype): 
        TIMEOUT = 5.0
        RETRIES = 0

        # dictionary for storing the results from the yummly api.
        meals = {}

        client = Client(api_id='f679e06d', api_key='b7d0fb2f961db4832b468523283d5bc0', timeout=TIMEOUT, retries=RETRIES)
        #search = client.search('breakfast') 
        #match = search.matches[0]                                                                                                                              
        param = {
                'q': mealtype,
                'start': 0,
                'maxResult': 10,
                'requirePicutres': True,
                'maxTotalTimeInSeconds': 3600,
                'nutrition.FAT.min': 0,
                'nutrition.FAT.max': 20
        }

        results = client.search(**param)
        for match in results.matches:
            meals[match.recipeName] = match.smallImageUrls
        return meals

"""def main():
    results1 = fetch_meals('breakfast')
    for k in results1:
        print k


if __name__ == '__main__':
    main()"""


    

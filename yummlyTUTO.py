from yummly import Client

# default option values
TIMEOUT = 5.0
RETRIES = 0

client = Client(api_id='f679e06d', api_key='b7d0fb2f961db4832b468523283d5bc0', timeout=TIMEOUT, retries=RETRIES)

search = client.search('green eggs and ham')
match = search.matches[0]

recipe = client.recipe(match.id)


results = client.search('bacon')

print 'Total Matches:', results.totalMatchCount
for match in results.matches:
	print match
    #print 'Recipe ID:', match.id
    #print 'Recipe:', match.recipeName
    #print 'Rating:', match.rating
    #print 'Total Time (mins):', match.totalTimeInSeconds / 60.0
    #print '----------------------------------------------------'



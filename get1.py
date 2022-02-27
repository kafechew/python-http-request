# importing the requests library
import requests
  
# api-endpoint
URL = "https://moopt.com/api/v1/models"
  
# location given here
apiKey = "ab84fdd454a49cace58fc5d826d548ae"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'api_key':apiKey}
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
  
# extracting data in json format
data = r.json()
  
  
# extracting latitude, longitude and formatted address 
# of the first matching location
#latitude = data['results'][0]['geometry']['location']['lat']
#longitude = data['results'][0]['geometry']['location']['lng']
#formatted_address = data['results'][0]['formatted_address']
  
# printing the output
#print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#      %(latitude, longitude,formatted_address))
print(data)

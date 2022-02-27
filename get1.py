# importing the requests library
import requests

request_headers = {
      "Accept-Language": "en-US,en;q=0.5",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Referer": "https://moopt.com",
      "Connection": "keep-alive" 
}
  
# api-endpoint
URL = "http://moopt.com/api/v1/solve"
    
# defining a params dict for the parameters to be sent to the API
PARAMS = {
      'api_key': 'ab84fdd454a49cace58fc5d826d548ae', 
      '_id': 'NxLpMHe8rFmSm8DP9',
      'solver': 'coinbc',
      'timeout': '60000',
      'dat': 'n = 5; \nd = array2d(Range, Range,[99999999,354,361,1490,2171,353,99999999,722,1170,1852,366,723,99999999,1859,2540,1490,1172,1859,99999999,686,2185,1867,2554,700,99999999]); \ncities = array1d(Range, ["KualaLumpur","GeorgeTown","RafflesAvenue","Bangkok","ChiangMai"]); \nlongitudes = array1d(Range, ["101.686855", "100.3287506", "103.8631368", "100.5017651", "98.9853008"]); \nlatitudes = array1d(Range, ["3.139003", "5.4141307", "1.2892988", "13.7563309", "18.7883439"]);'
}
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS, headers = request_headers)
  
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

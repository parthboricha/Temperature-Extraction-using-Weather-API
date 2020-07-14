import requests
import json

url = "https://api.weather.gov/points/38.2527,-85.7585/forecast"
url1 = "https://api.weather.gov/points/42.3601,-71.0589/forecast"
url2 = "https://api.weather.gov/points/39.1031,-84.5120/forecast"
 
response = requests.get(url)
response1 = requests.get(url1)
response2 = requests.get(url2)

data = response.text
data1 = response1.text
data2 = response2.text

parsed = json.loads(data)
parsed1 = json.loads(data1)
parsed2 = json.loads(data2)

print(json.dumps(parsed["properties"]["periods"][3]["temperature"]), ",",  json.dumps(parsed1["properties"]["periods"][3]["temperature"]), ",",  json.dumps(parsed2["properties"]["periods"][3]["temperature"]))

# OUTPUT: 74 , 61 , 73

import requests
import json

city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=ccb7abe927e142e883f101017241402&q= {city}"

r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
print(wdic["current"]["condition"]["text"])
print(wdic["current"]["humidity"])

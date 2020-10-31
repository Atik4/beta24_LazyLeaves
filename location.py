from selenium import webdriver
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from selenium import webdriver

location_from = "indore"
location_to = "bhopal"

response_from = requests.get("https://nominatim.openstreetmap.org/?addressdetails=1&q="+location_from+"&format=json&limit=1")
response_to = requests.get("https://nominatim.openstreetmap.org/?addressdetails=1&q="+location_to+"&format=json&limit=1")

response_from.json()

lat_from = response_from.json()[0]['lat']
lon_from = response_from.json()[0]['lon']

lat_to = response_to.json()[0]['lat']
lon_to = response_to.json()[0]['lon']

print(lat_from,lon_from)
print(lat_to,lon_to)

response_route = requests.get('http://www.mapquestapi.com/directions/v2/route?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&from='+lat_to+','+lon_to+'&to='+lat_from+','+lon_from)

direction = [ "none","north","northwest","northeast","south","southeast","southwest","west","east"]
turnType = ["straight","slight right","right","sharp right","reverse","sharp left","left","slight left","right u-turn","left u-turn","right merge","left merge","right on ramp","left on ramp","right off ramp","left off ramp","right fork","left fork","straight fork"]
for i in response_route.json()["route"]["legs"][0]["maneuvers"]:
    s1 = "Take " + turnType[i["turnType"]]+" and go "+ str(int(i["distance"]*1000)) + " meters, in " + direction[i["direction"]] + " direction"
    s2 = i["narrative"]
    
    print(s1)
    print(s2,end="\n\n")










# open_street_url = 'http://www.mapquestapi.com/directions/v2/route?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&from='+lat_to+','+lon_to+'&to='+lat_from+','+lon_from
# my_url = "http://www.mapquestapi.com/directions/v2/route?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&from=22.7196,75.8577&to=23.23366135,77.43025057797232"

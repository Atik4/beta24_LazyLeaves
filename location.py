import requests

location_from = "Indore"
location_to = "Bhopal"

response_from = requests.get("https://nominatim.openstreetmap.org/?addressdetails=1&q="+location_from+"&format=json&limit=1")
response_to = requests.get("https://nominatim.openstreetmap.org/?addressdetails=1&q="+location_to+"&format=json&limit=1")
response_route = requests.get("https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&route=22.7200%2C75.8680%3B23.2580%2C77.4020#map=9/22.9976/76.6351")

print(response_from.content)
print(response_to.content)
print(response_route)

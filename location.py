import requests


location_from = "indore"
location_to = "db mall bhopal"
near_me = "mall"

response_from = requests.get("https://nominatim.openstreetmap.org/?addressdetails=1&q="+location_from+"&format=json&limit=1")
response_to = requests.get("https://nominatim.openstreetmap.org/?addressdetails=1&q="+location_to+"&format=json&limit=1")
lat_from = response_from.json()[0]['lat']
lon_from = response_from.json()[0]['lon']

query_type = 1

if query_type==0:

    lat_to = response_to.json()[0]['lat']
    lon_to = response_to.json()[0]['lon']

    response_route = requests.get(
        'http://www.mapquestapi.com/directions/v2/route?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&from=' + lat_from + ',' + lon_from + '&to=' + lat_to + ',' + lon_to)
    print("Start Point:", location_from, lat_from, lon_from)
    print("End Point:", location_to, lat_to, lon_to)
    direction = [ "none","north","northwest","northeast","south","southeast","southwest","west","east"]
    turnType = ["straight","slight right","right","sharp right","reverse","sharp left","left","slight left","right u-turn","left u-turn","right merge","left merge","right on ramp","left on ramp","right off ramp","left off ramp","right fork","left fork","straight fork"]

    for i in response_route.json()["route"]["legs"][0]["maneuvers"]:
        s1 = "Take " + turnType[i["turnType"]]+" and go "+ str(int(i["distance"]*1609)) + " meters, in " + direction[i["direction"]] + " direction"
        s2 = i["narrative"]

        print(s1)
        print(s2,end="\n\n")

elif query_type == 1:
    r= requests.get('http://open.mapquestapi.com/nominatim/v1/search.php?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&format=json&q='+lat_from + ',' + lon_from +'+['+near_me+']&addressdetails=1&limit=20')
    print(r.json())
    for i in r.json():
        print(i["display_name"])










# open_street_url = 'http://www.mapquestapi.com/directions/v2/route?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&from='+lat_to+','+lon_to+'&to='+lat_from+','+lon_from
# my_url = "http://www.mapquestapi.com/directions/v2/route?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&from=22.7196,75.8577&to=23.23366135,77.43025057797232"

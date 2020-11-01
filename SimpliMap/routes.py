import requests

def route1(source, destination):
    location_from = source
    location_to = destination

    response_from = requests.get(
        "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + location_from + "&format=json&limit=1")
    response_to = requests.get(
        "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + location_to + "&format=json&limit=1")

    lat_from = response_from.json()[0]['lat']
    lon_from = response_from.json()[0]['lon']

    lat_to = response_to.json()[0]['lat']
    lon_to = response_to.json()[0]['lon']

    ans = ""

    response_route = requests.get(
        'http://www.mapquestapi.com/directions/v2/route?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&from=' + lat_from + ',' + lon_from + '&to=' + lat_to + ',' + lon_to)
    print("Start Point:", location_from, lat_from, lon_from)
    print("End Point:", location_to, lat_to, lon_to)
    direction = ["none", "north", "northwest", "northeast", "south", "southeast", "southwest", "west", "east"]
    turnType = ["straight", "slight right", "right", "sharp right", "reverse", "sharp left", "left", "slight left",
                "right u-turn", "left u-turn", "right merge", "left merge", "right on ramp", "left on ramp",
                "right off ramp", "left off ramp", "right fork", "left fork", "straight fork"]

    for i in response_route.json()["route"]["legs"][0]["maneuvers"]:
        s1 = "Take " + turnType[i["turnType"]] + " and go " + str(int(i["distance"] * 1609)) + " meters, in " + \
             direction[i["direction"]] + " direction"
        s2 = i["narrative"]
        ans += s1 + '\n' + s2 + '\n\n'
        # print(s1)
        # print(s2, end="\n\n")

    ans = ans.strip()
    print(ans)
    return ans

def route2(source, near_me):
    location_from = source
    ans = ''
    response_from = requests.get(
        "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + location_from + "&format=json&limit=1")
    lat_from = response_from.json()[0]['lat']
    lon_from = response_from.json()[0]['lon']
    r = requests.get(
        'http://open.mapquestapi.com/nominatim/v1/search.php?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&format=json&q=' + lat_from + ',' + lon_from + '+[' + near_me + ']&addressdetails=1&limit=20')
    print(r.json())
    for i in r.json():
        ans += i["display_name"] + '\n'
    # print(i["display_name"])


    ans = ans.strip()
    print(ans)
    return ans
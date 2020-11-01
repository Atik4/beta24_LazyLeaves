# from future import print_function
# import json
# import boto3

# client = boto3.client('lambda')

# def lambda_handler(event, context):

#     print("Received event: " + str(event))
#     inputForInvoker = {'To': '+919079945319', 'From': '+13345131650', 'body': 'this is the path' }

# 	response = client.invoke(FunctionName='arn:aws:lambda:us-east-1:389772381755:function:sendsms',
# 		       InvocationType='RequestResponse',Payload=json.dumps(inputForInvoker))

# 	responseJson = json.load(response['Payload'])

# 	print('\n')
# 	print(responseJson)
# 	print('\n')
#     return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
#           '<Response><Message><Body>Hello world! -Lambda</Body><Media>https://d...content-available-to-author-only...o.com/owl.png</Media></Message></Response>'


import base64
import json
import os
import urllib
import requests
from urllib import request, parse
from botocore.vendored import requests


TWILIO_SMS_URL = "https://a...content-available-to-author-only...o.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


def lambda_handler(event, context):
    to_number = "+919079945319"
    from_number = "+13345131650"
    location_from = "indore"
    location_to = "db mall bhopal"
    near_me = "colleges"

    response_from = requests.get(
        "https://n...content-available-to-author-only...p.org/?addressdetails=1&q=" + location_from + "&format=json&limit=1")
    response_to = requests.get(
        "https://n...content-available-to-author-only...p.org/?addressdetails=1&q=" + location_to + "&format=json&limit=1")
    lat_from = response_from.json()[0]['lat']
    lon_from = response_from.json()[0]['lon']

    query_type = 1
    ans = ""

    if query_type == 0:

        lat_to = response_to.json()[0]['lat']
        lon_to = response_to.json()[0]['lon']

        response_route = requests.get(
            'http://w...content-available-to-author-only...i.com/directions/v2/route?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&from=' + lat_from + ',' + lon_from + '&to=' + lat_to + ',' + lon_to)
        print("Start Point:", location_from, lat_from, lon_from)
        print("End Point:", location_to, lat_to, lon_to)
        direction = ["none", "north", "northwest", "northeast", "south", "southeast", "southwest", "west", "east"]
        turnType = ["straight", "slight right", "right", "sharp right", "reverse", "sharp left", "left", "slight left",
                    "right u-turn", "left u-turn", "right merge", "left merge", "right on ramp", "left on ramp",
                    "right off ramp", "left off ramp", "right fork", "left fork", "straight fork"]

        for obb in response_route.json()["route"]["legs"][0]["maneuvers"]:
            s1 = "Take " + turnType[obb["turnType"]] + " and go " + str(int(obb["distance"] * 1609)) + " meters, in " + \
                 direction[obb["direction"]] + " direction"
            s2 = obb["narrative"]
            ans += s1 + '\n' + s2 + '\n\n'
        # print(s1)
        # print(s2, end="\n\n")

    elif query_type == 1:
        r = requests.get(
            'http://o...content-available-to-author-only...i.com/nominatim/v1/search.php?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&format=json&q=' + lat_from + ',' + lon_from + '+[' + near_me + ']&addressdetails=1&limit=20')
        print(r.json())
        for obb in r.json():
            ans += obb["display_name"] + '\n'
        # print(i["display_name"])

    ans = ans.strip()
    print(ans)
    body = ans
    #print(body)
    print(event)

    if not TWILIO_ACCOUNT_SID:
        return "Unable to access Twilio Account SID."
    elif not TWILIO_AUTH_TOKEN:
        return "Unable to access Twilio Auth Token."
    elif not to_number:
        return "The function needs a 'To' number in the format +12023351493"
    elif not from_number:
        return "The function needs a 'From' number in the format +19732644156"
    elif not body:
        return "The function needs a 'Body' message to send."

    # insert Twilio Account SID into the REST API URL
    populated_url = TWILIO_SMS_URL.format(TWILIO_ACCOUNT_SID)
    post_params = {"To": to_number, "From": from_number, "Body": body}

    # encode the parameters for Python's urllib
    data = parse.urlencode(post_params).encode()
    req = request.Request(populated_url)

    # add authentication header to request based on Account SID + Auth Token
    authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    base64string = base64.b64encode(authentication.encode('ascii'))
    req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))

    try:
        # perform HTTP POST request
        with request.urlopen(req, data) as f:
            print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
    except Exception as e:
        # something went wrong!
        return e

    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>' \
           '<Response><Message><Body>Hello world! -Lambda</Body></Message></Response>'
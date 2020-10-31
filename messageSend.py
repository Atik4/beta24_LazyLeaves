# from __future__ import print_function
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
#           '<Response><Message><Body>Hello world! -Lambda</Body><Media>https://demo.twilio.com/owl.png</Media></Message></Response>'


import base64
import json
import os
import urllib
from urllib import request, parse
from botocore.vendored import requests


TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


def lambda_handler(event, context):
    response_from = requests.get("http://www.mapquestapi.com/directions/v2/route?key=j1IVnoFZUzzkteLml8NKw1wjF5x5mGK3&from=22.7196,75.8577&to=23.23366135,77.43025057797232")
    #print(response_from.json())
    to_number = "+919079945319"
    print(to_number)
    from_number = "+13345131650"
    body = event['Body']
    print(body)
    print(response_from.content)
    
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

    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
           '<Response><Message><Body>Hello world! -Lambda</Body></Message></Response>'
    

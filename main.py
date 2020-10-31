from extract import find_src_dest
from process import preprocess
from routes import route1, route2


response = {'ToCountry': 'US', 'ToState': 'AZ', 'SmsMessageSid': 'SM994801c6ee52cb08db6affa285661e12', 'NumMedia': '0',
            'ToCity': 'PHOENIX', 'FromZip': '85087', 'SmsSid': 'SM994801c6ee52cb08db6affa285661e12',
            'FromState': 'AZ', 'SmsStatus': 'received', 'FromCity': 'PHOENIX',
            'Body': 'travel from Nariman Point Mumbai to Bandra East Mumbai',
            'FromCountry': 'US', 'To': '%2B14804284194', 'ToZip': '85034', 'NumSegments': '1',
            'MessageSid': 'SM994801c6ee52cb08db6affa285661e12',
            'AccountSid': 'ACffa2ba37390d2cc87d8b52bf6d869c2a', 'From': '%2B16022886791', 'ApiVersion': '2010-04-01'}
test_string = response['Body']
message_body = preprocess(test_string)
source, destination = find_src_dest(message_body)

# route1(source, destination)
print(source, destination)
near_me = "mechanic"
route2(source, near_me)


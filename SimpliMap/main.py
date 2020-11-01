from extract import find_src_dest, find_src
from process import preprocess
from routes import route1, route2
from util import find_query_type, near_locs


response = {'ToCountry': 'US', 'ToState': 'AZ', 'SmsMessageSid': 'SM994801c6ee52cb08db6affa285661e12', 'NumMedia': '0',
            'ToCity': 'PHOENIX', 'FromZip': '85087', 'SmsSid': 'SM994801c6ee52cb08db6affa285661e12',
            'FromState': 'AZ', 'SmsStatus': 'received', 'FromCity': 'PHOENIX',
            'Body': 'get directions from andheri mumbai to bandra mumbai',
            'FromCountry': 'US', 'To': '%2B14804284194', 'ToZip': '85034', 'NumSegments': '1',
            'MessageSid': 'SM994801c6ee52cb08db6affa285661e12',
            'AccountSid': 'ACffa2ba37390d2cc87d8b52bf6d869c2a', 'From': '%2B16022886791', 'ApiVersion': '2010-04-01'}
test_string = response['Body']
message_body = preprocess(test_string)

query_type = find_query_type(message_body)
# print(query_type)
ans = ""
if query_type == 1:
    source, destination = find_src_dest(message_body)
    print(source, destination)
    ans = route1(source, destination)
else:
    # source, destination = find_src_dest(message_body)
    message_body = message_body.lower()
    near_me, query = near_locs(message_body)
    source = find_src(query)
    print('near me: ', near_me)
    print('source:', source)
    ans = route2(source, near_me)


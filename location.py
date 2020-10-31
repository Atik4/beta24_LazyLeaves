import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

query = "I am currently standing on Mata Mandir Bhopal get directions to DB Mall Bhopal"

query_response_analyser = requests.post("http://api.intellexer.com/analyzeText?apiKey=25e240b9-cb35-47ec-9a80-25172c04e228",
                               data=query)

analyser_token =[]
nouns=[]
prepositions=[]
tokens= []
start_prepositions = ["from","on","at"]
end_prepositions = ["to"]
result=[]
for i in query_response_analyser.json()['sentences'][0]['tokens']:
    tokens.append(i['text']['content'])
    analyser_token.append(i["partOfSpeechTag"])
    result.append([i['text']['content'],i["partOfSpeechTag"]])
    # if i["partOfSpeechTag"] in ["NN","NNS","NNP","NNPS"]:
    #     nouns.append(i["text"]['content'])
    if i["partOfSpeechTag"] in ["IN"]:
        prepositions.append(i["text"]['content'])
        if i["text"]["content"] in start_prepositions:
            start = i["text"]["content"]
        elif i["text"]["content"] in end_prepositions:
            end = i["text"]["content"]



print(query)
print("tokens", tokens)
print("analysers", analyser_token)
print(result)

start_index =   tokens.index(start)
end_index =     tokens.index(end)

for i in result[start_index+1:]:
    if i[1] in ["NN","NNS","NNP","NNPS"]:
        source=i[0]
        break

for i in result[end_index+1:]:
    if i[1] in ["NN","NNS","NNP","NNPS"]:
        destination=i[0]
        break

print(source, destination)
# print(nouns)
# print(prepositions)

query_response_summeriser = requests.post("http://api.intellexer.com/summarizeText?apikey=3f772cc7-5773-4a2f-8f8d-a9da42a8ed3c&summaryRestriction=7&returnedTopicsCount=2&loadConceptsTree=true&loadNamedEntityTree=true&usePercentRestriction=true&conceptsRestriction=7&structure=general&fullTextTrees=true&textStreamLength=1000&wrapConcepts=true",
                               data=query)
summarize_token = []
for i in query_response_summeriser.json()['items']:
    summarize_token.append(i['text'])
clusters=[]
print(summarize_token)
for i in summarize_token:
    html_doc = i
    page_soup = soup(html_doc, "html.parser")
    containers = page_soup.findAll("b")

    for container in containers:
        clusters.append(container.text)

    clusters.sort(reverse=True)
    print(clusters)
    for i in clusters:
        if i.find(source)!=-1:
            source = i
        if i.find(destination)!=-1:
            destination = i

print(source, destination)


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

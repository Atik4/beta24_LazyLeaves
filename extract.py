
import requests

def find_src_dest(query_string):

    query = query_string
    # query = "I want to travel from Bandra East Mumbai to Bandra West Mumbai"
    query_response_analyser = requests.post(
        "http://api.intellexer.com/analyzeText?apiKey=25e240b9-cb35-47ec-9a80-25172c04e228",
        data=query)

    analyser_token = []
    prepositions = []
    tokens = []
    start_prepositions = ["from", "on", "at"]
    end_prepositions = ["to"]
    result = []
    for i in query_response_analyser.json()['sentences'][0]['tokens']:
        tokens.append(i['text']['content'])
        analyser_token.append(i["partOfSpeechTag"])
        result.append([i['text']['content'], i["partOfSpeechTag"]])
        # if i["partOfSpeechTag"] in ["NN","NNS","NNP","NNPS"]:
        #     nouns.append(i["text"]['content'])
        if i["partOfSpeechTag"] in ["IN"]:
            prepositions.append(i["text"]['content'])
            if i["text"]["content"] in start_prepositions:
                start = i["text"]["content"]
            elif i["text"]["content"] in end_prepositions:
                end = i["text"]["content"]

    # print(query)
    print("tokens", tokens)
    print("analysers", analyser_token)

    i = 0
    while i < len(result):
        if result[i][1] == result[i - 1][1] and result[i][1] == 'NN':
            result[i - 1][0] = result[i - 1][0] + " " + result[i][0]
            result.remove(result[i])
            tokens[i - 1] = tokens[i - 1] + tokens[i]
            tokens.remove(tokens[i])
            i = i - 1
        i += 1

    print(result)

    start_index = tokens.index(start)
    end_index = tokens.index(end)

    print(start_index, end_index, len(result))
    source = ""
    destination = ""

    for i in result[start_index:]:
        if i[1] in ["NN", "NNS", "NNP", "NNPS"]:
            source = i[0]
            break

    for i in result[end_index:]:
        if i[1] in ["NN", "NNS", "NNP", "NNPS"]:
            destination = i[0]
            break

    print(source, destination)
    return (source, destination)

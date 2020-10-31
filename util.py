def find_query_type(query_string):
    synonyms = ['near', 'nearby', 'near by', 'around']
    query_type = 1
    flag = False
    for synonym in synonyms:
        if query_string.find(synonym) != -1:
            query_type = 2
            return query_type
    return query_type

def near_locs(query):
    near_me = ""
    locations = {
        "bank": ["banks", "Banks", "bank", "Bank"],
        "mall": ["malls", "shopping centers", "plazas", "shopping malls", "mall", "shopping center", "plaza", "shopping mall"],
        "airport": ["airport", "aerodrome", "airdrome"],
        "hotel": ["hotels", "hotel"],
        "doctor": ["doctors", "doctor", "doc", "physician"],
        "hospital": ["hospitals", "hospital"],
        "cafe": ["coffee house", "coffee shop", "cafes", "cafe"],
        "college": ["colleges", "college"],
        "restaurant": ["restaurants", "eating places", "eating place", "eating house"],
        "post office": ["post office"],
        "mechanic": ["automobile_mechanic", "mechanics", "mechanic", "machinist", "car-mechanic", "shop_mechanic"],
        "monument": ["monuments", "monument"],
        "school": ["schools", "school"],
        "university": ["universities", "university"],
        "police": ["police station", "police"]
    }

    removed_words = ['search', 'find', 'look', 'places', 'place']

    for key, values in locations.items():
        flag = False
        for value in values:
            if query.find(value) != -1:
                near_me = key
                discard_noun = value

                query = query.replace(discard_noun, '')
                flag = True
                break
        if flag:
            break
    for value in removed_words:
        if query.find(value) != -1:
            query = query.replace(value, '')
    print(near_me)
    # print(query)
    return near_me, query

if __name__ == '__main__':
    query = "search for cafes near Mata Mandir Bhopal"
    query = query.lower()
    # print(query.lower())
    near_me, query = near_locs(query)
    print(near_me)
    query.strip()
    print(query)
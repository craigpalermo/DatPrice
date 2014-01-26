from ebaysdk import finding

import json

APPID = "CraigPal-4fe7-42b8-b29a-be707becdb0b" 

def get_search_results_json(keywords, categoryId):
    api = finding(appid=APPID)
    api.execute('findCompletedItems', {'keywords': keywords, \
                                       'categoryId': categoryId, \
                                       'Condition': '3000', \
                                       'soldItemsOnly': 'true', 
                                       'sortOrder': 'EndTimeSoonest'})
    temp = api.response_dict()
    if temp.get('searchResult') != None and temp.get('searchResult').get('item') != None:
        json_string = json.dumps(temp.get('searchResult').get('item'))
    else:
        json_string = ""

    return json_string

def get_similar_listings(keywords, categoryId):
    api = finding(appid=APPID)
    api.execute('findItemsAdvanced', {'keywords': keywords, 
                         'categoryId': categoryId, 
                         'ListingType': 'FixedPrice',
                         'soldItemsOnly': 'false', 
                         'sortOrder': 'EndTimeSoonest'})

    temp = api.response_dict()
    if temp.get('searchResult') != None and temp.get('searchResult').get('item') != None:    
        json_string = json.dumps(temp.get('searchResult').get('item'))
    else:
        json_string = ""
    
    return json_string

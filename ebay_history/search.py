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
    json_string = json.dumps(api.response_dict().get('searchResult').get('item'))
    return json_string

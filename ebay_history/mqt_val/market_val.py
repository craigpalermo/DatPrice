import json
import search_json



def det_mv(item):
    name = item["title"]["value"]
    name = name [:len(name)/2]

    cat = item["categoryId"]["value"]
    cond = item["conditionDisplayName"]["value"]
    
    name = cond + name

      

def determine_below_mqt_val(search_in, cat):

    title = title[:len(title)/2]


    api = finding(appid=APPID)
    api.execute('findCompletedItems', {'keywords': search_in, \
                                       'categoryId': cat, \
                                       'Condition': '3000', \
                                       'soldItemsOnly': 'true',
                                       'sortOrder': 'EndTimeSoonest'})

    results = search_json.get_search_results_json(title, cat)
    total_values = 0
    avg = 0
    for result in results:
        print result
        curr_mv = det_mv(result)
        print curr_mv

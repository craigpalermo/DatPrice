import json
import search_json
import urllib2
from ebaysdk import finding

APPID = "CraigPal-4fe7-42b8-b29a-be707becdb0b"


def det_mv(name):
    request_url = "http://us.api.invisiblehand.co.uk/v1/products?app_id=2226a647&app_key=de0d3c4c34156a0abaaab69b61e9643a&query=" 

    name = name.replace("+", " ")
    name = name.replace("*", " ")
    name = name.replace("&", " ")
    name = name.replace("(", " ")
    name = name.replace(")", " ")


    name = name.replace(" ", "%20")

    request_url += name
    
    try:
        json_in = json.loads(urllib2.urlopen(request_url).read())
    except:
        return -2


    items = json_in["results"]

    avg = 0
    total_items = 0


    for curr_item in items:
        total_items += 1

        if("best_page" in curr_item):
            avg += float(curr_item["best_page"]["price"])
            continue
        elif("price" in curr_item):
            avg += float(curr_item["price"])
            continue
        else:
            total_items -=1
    
    if (total_items ==0):
        return -1


    avg = avg/total_items
    
    return avg
    
          

def determine_below_mqt_val(search_in, cat):

    api = finding(appid=APPID)
    api.execute('findCompletedItems', {'keywords': search_in, \
                                       'categoryId': cat, \
                                       'Condition': '3000', \
                                       'soldItemsOnly': 'true',
                                       'sortOrder': 'EndTimeSoonest'})

    results = search_json.get_search_results_json(search_in, cat)
    total_values = 0
    avg = 0

    neg_run = 0

    ret = []

    for result in results:
        curr_mv = det_mv(result["title"]["value"])

        if (curr_mv < 0):
            neg_run += 1
            if (neg_run > 10):
                break
        else:
            ret.append({"MarketPrice": curr_mv,
            "ProductTitle" : result["title"]["value"],
            "ListPrice" : result["sellingStatus"]["convertedCurrentPrice"]["value"], 
            "URL" : result["viewItemURL"]["value"]
            })


    return {"Matches" : ret}
        


import json
import search_json
import urllib2
from ebaysdk import finding

APPID = "CraigPal-4fe7-42b8-b29a-be707becdb0b"

def main():
    query = raw_input("Search Term: ")
    category = int(raw_input("CategoryID"))

    determine_below_mqt_val(query, category)

def det_mv(item):
    request_url = "http://us.api.invisiblehand.co.uk/v1/products?app_id=2226a647&app_key=de0d3c4c34156a0abaaab69b61e9643a&query=" 

    name = item["title"]["value"]
    name = name [:len(name)/2]

    cond = item["condition"]["conditionDisplayName"]["value"]
    
    name = cond + name

    name = name.replace(" ", "%20")

    request_url += name
    json_in = json.loads(urllib2.urlopen(request_url).read())

    items = json_in["results"]

    avg = 0
    total_items = json_in["info"]["total_results"]

    if (total_items == 0):
        return -1

    for curr_item in items:
        avg += int(curr_item["best_page"]["pnp"])

    avg /= total_items
    
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
    for result in results:
        curr_mv = det_mv(result)
        print curr_mv
        print result["title"]["value"]




main()


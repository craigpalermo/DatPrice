from ebaysdk import finding

import json
import datetime

APPID = "CraigPal-4fe7-42b8-b29a-be707becdb0b"

def get_listings_to_buy_json(category):
	#initialize timer
	myObject = datetime.datetime.utcnow() + datetime.timedelta(seconds=1800)
	ebayObject = myObject.strftime("%Y-%m-%d" + "T" + "%H:%M:%S.000Z")
	api = finding(appid=APPID)
	api.execute('findItemsAdvanced', {'categoryId': category, \
										'EndTimeTo': ebayObject, \
										'SortOrderType': "PricePlusShippingLowest"})
	json_string = json.dumps(api.response_dict().get('searchResult').get('item'))
	return json_string
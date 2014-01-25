from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

from search import get_search_results_json, get_similar_listings
from datetime import datetime
from time import mktime
from operator import itemgetter

import json, time

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        data = {'show_graph': False}
        return render(request, self.template_name, data) 

    def post(self, request):
        keywords = request.POST.get('keywords')
        categoryId = request.POST.get('categoryId')
        json_string = get_search_results_json(keywords, categoryId)
        #return HttpResponse(json_string)
        
        results = json.loads(json_string)
        
        values = []
        for item in results:
            time_string = item.get('listingInfo').get('endTime').get('value')
            time_format = "%Y-%m-%dT%H:%M:%S.000Z"
            end_time = time.strptime(time_string, time_format)
            end_time = datetime.fromtimestamp(mktime(end_time))
            price = item['sellingStatus']['currentPrice']['value']
            values.append({'end_time': end_time, 'value': float(price)})
        
        items_by_hour = {}
        for item in values:
            hour = item['end_time'].hour
            if hour in items_by_hour:
                items_by_hour[hour].append(item)
            else:
                items_by_hour[hour] = [item]

        averages = {}
        for hour in items_by_hour:
            sum = 0
            for item in items_by_hour[hour]:
                sum += item['value']
            average = sum / len(items_by_hour[hour])
            averages[hour] = average
        sorted_averages = sorted(averages.iteritems())

        # calculate average price
        sum = 0
        for item in sorted_averages:
            sum += item[1]
        average_price = sum / len(sorted_averages)

        data = {
            "averages": sorted_averages,
            "average_price": average_price,
            "show_graph": True
        }
        return render(request, self.template_name, data)


class SimilarView(View):
    template_name = 'similar-listings.html'

    def post(self, request):
        keywords = request.POST.get('keywords')
        categoryId = request.POST.get('categoryId')
        json_string = get_similar_listings(keywords, categoryId)
        results = json.loads(json_string)
        
        values = []
        for item in results:
            values.append(item['title']['value'])
        print values 
        data = {
            "items": values,
        }
        return render(request, self.template_name, data)

from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

from search import get_search_results_json

import json

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name, None) 

    def post(self, request):
        keywords = request.POST.get('keywords')
        categoryId = request.POST.get('categoryId')
        json_string = get_search_results_json(keywords, categoryId)
        return HttpResponse(json_string)


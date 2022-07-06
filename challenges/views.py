from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def mounthly_challenge(request, month):
    months = {
        "january": "Eat no meat for entire month :)",
        "february": "Walk for at least 20 minutes everyday :P",
        "march": "Learn Django for at least 20 minutse every day :D",

    }
    if month in months.keys():
        return HttpResponse(months[month])
    else:
        return HttpResponseNotFound("This month is not supported :(")


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

months = {
    "january": "Eat no meat for entire month :)",
    "february": "Walk for at least 20 minutes every day :P",
    "march": "Learn Django for at least 20 minutse every day :D",
    "april" : "Drink milk every day",
    "may" :  "Do meditation every day",
    "june" : "Learn 10 new word every day",
    "july" : "Say somthing good to someone everyday",
    "august" : "No sweet for month",
    "september" : "Watch one tedtalk every day",
    "october" : "wake up early every day",
    "november" : "do skin routin every day ",
    "december" : "read 10 page book every day"
    }

def monthly_challenge_by_number(request,month):
    l_month = list(months.keys())
    if month > len(l_month):
        return HttpResponseNotFound("Invalid month")
    redirect_month = l_month[month-1]
    return HttpResponseRedirect("/challenges/"+ redirect_month)

def mounthly_challenge(request, month):
    
    if month in months.keys():
        return HttpResponse(months[month])
    else:
        return HttpResponseNotFound("This month is not supported :(")


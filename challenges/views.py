import imp
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

months = {
    "january": "Eat no meat for entire month :)",
    "february": "Walk for at least 20 minutes every day :P",
    "march": "Learn Django for at least 20 minutse every day :D",
    "april": "Drink milk every day",
    "may":  "Do meditation every day",
    "june": "Learn 10 new word every day",
    "july": "Say somthing good to someone everyday",
    "august": "No sweet for month",
    "september": "Watch one tedtalk every day",
    "october": "wake up early every day",
    "november": "do skin routin every day ",
    "december": "read 10 page book every day"
}


def index(request):
    list_items = ""
    l_months = list(months.keys())
    for month in l_months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challange", args=[month])
        list_items += f"<li><a href= \"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
def monthly_challenge_by_number(request, month):
    l_month = list(months.keys())
    if month > len(l_month):
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    redirect_month = l_month[month-1]
    redirect_path = reverse("monthly-challange",args=[redirect_month]) #/challange/june
    return HttpResponseRedirect(redirect_path)


def mounthly_challenge(request, month):

    if month in months.keys():
        text_return = months[month]
        response_data = f"<h1>{text_return}</h1>"
        return HttpResponse(response_data)
    else:
        return HttpResponseNotFound("<h1>This month is not supported :(</h1>")

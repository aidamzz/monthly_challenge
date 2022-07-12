from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}


def index(request):
    list_items = ""
    l_months = list(months.keys())

    return render(request, "challenges/index.html",{
        "months": l_months
    })


def monthly_challenge_by_number(request, month):
    l_month = list(months.keys())
    if month > len(l_month):
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    redirect_month = l_month[month-1]
    redirect_path = reverse("monthly-challange",
                            args=[redirect_month])  # /challange/june
    return HttpResponseRedirect(redirect_path)


def mounthly_challenge(request, month):

    if month in months.keys():
        text_return = months[month]
        return render(request, "challenges/challenge.html", {
            "text": text_return,
            "name_month": month

        })
    else:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

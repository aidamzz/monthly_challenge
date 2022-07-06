from django.urls import path
from . import views

urlpatterns = [
    path("<month>", views.mounthly_challenge)
]

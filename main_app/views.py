from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect, JsonResponse
from .models import Coustomer
from datetime import datetime, timedelta
from .models import *
from django.urls import reverse
from django.contrib import messages
import stripe

# Create your views here.
api = "sk_test_51NgRdTIB9nny6800bEHUeDgzPMnya3ZSjdX4aoY2Bexfm1EHRc204sOPnxGt6f3aQGpbAe8wmvuZ3QZW11gOGHtd00IKJmL7UN"


# customer = stripe.Customer.retrieve(
#   "cu_1Nh9r6IB9nny6800WMaMJPz8",
#   api_key="sk_test_51NgRdTIB9nny6800bEHUeDgzPMnya3ZSjdX4aoY2Bexfm1EHRc204sOPnxGt6f3aQGpbAe8wmvuZ3QZW11gOGHtd00IKJmL7UN"
# )
# customer.capture() # Uses the same API Key.


def index(request):
    return render(request=request, template_name="pages/index.html")


def user_info(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        username = request.POST.get("name")
        usernumber = request.POST.get("number")
        vorC = request.POST.get("vorC")
        time = request.POST.get("time")
        all_data = Coustomer(
            UserName=username,
            UserNum=usernumber,
            Amount=18,
            PymentWay=vorC,
            Time="2006-10-25 14:30:59",
        )
        all_data.save()
        return HttpResponseRedirect("/bill.html")
    return render(
        request=request,
        template_name="pages/user_info.html",
    )


def bill(request):
    return render(
        request=request,
        template_name="pages/bill.html",
        context={"name": Coustomer.objects.latest("id")},
    )


def boking(request):
    # Only show the days that are not full:
    return render(
        request,
        "pages/boking.html",
    )

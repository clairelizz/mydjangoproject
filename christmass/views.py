from django.shortcuts import render

import datetime

from django.http import HttpResponse

# Create your views here.

def christmass(request):
    now = datetime.datetime.now()
    return render(request, "this.html", {
        "new": now.month == 4 and now.day == 4
    })
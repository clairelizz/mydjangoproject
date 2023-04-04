from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def eMobilis(request):
    return HttpResponse("This is eMobilis")
def home(request):
    return render(request, 'home.html')

from django.http import HttpResponse
from django.shortcuts import render


def home(req): 
    # return HttpResponse("This is home page")
    return render(req,"index.html")
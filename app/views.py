from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def srujana(request):
    return HttpResponse('<marquee><h1>hiii hello tinava unava</marquee></h1>')
def meghana(request):
    return HttpResponse('<b>mama kutty</b>')


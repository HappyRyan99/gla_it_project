from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<a href=\"https://www.bilibili.com\">Bilibili</a><br/><a href='/rango/about/'>About</a><br/><a href='/rango/'>Index</a>")

def page_not_found(request):
    return HttpResponse(404)

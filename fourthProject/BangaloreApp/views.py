from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def corona_vijayanagar(request):
	data='<h1>corona case in vijayanagar:5000</h1>'
	return HttpResponse(data)

def corona_jayanagar(request):
	data='<h1>corona case in jayanagar:8000</h1>'
	return HttpResponse(data)

def corona_rajajinagar(request):
	data='<h1>corona case in rajajinagar:7000</h1>'
	return HttpResponse(data)

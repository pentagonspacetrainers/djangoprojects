from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def corona_vijayanagar(request):
	data='<h1>corona case in vijayanagar:4500</h1>'
	return HttpResponse(data)

def corona_kdroad(request):
	data='<h1>corona case in kdroad:6500</h1>'
	return HttpResponse(data)

def corona_rknagar(request):
	data='<h1>corona case in rknagar:7500</h1>'
	return HttpResponse(data)

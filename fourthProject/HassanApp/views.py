from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def corona_satyamangala(request):
	data='<h1>corona case in satyamangala:3900</h1>'
	return HttpResponse(data)

def corona_crpatna(request):
	data='<h1>corona case in crpatna:3700</h1>'
	return HttpResponse(data)

def corona_arsikere(request):
	data='<h1>corona case in arsikere:5500</h1>'
	return HttpResponse(data)

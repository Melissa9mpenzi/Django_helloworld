from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def contactPage(request):
    return HttpResponse("Contact Page")

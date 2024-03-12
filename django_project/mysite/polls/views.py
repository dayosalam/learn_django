from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, Wolrd. You are in poll s index.  ')
# Create your views here.

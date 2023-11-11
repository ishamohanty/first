from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jampandu1(request):
    return HttpResponse('Hi how are you')

def jampandu2(request):
    return HttpResponse('Hi how are you 2')
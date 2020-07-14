from django.shortcuts import render
from django.http import HttpResponse

def demo_01(request):
    return HttpResponse("hello word hello word")


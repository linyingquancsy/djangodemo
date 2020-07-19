from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse


def get_user_profiles(request):
    if request.method == 'POST':
        myFile = request.FILES.get("filename", None)
        if myFile:
            dir = os.path.join(os.path.join(settings.BASE_DIR, 'static'),'profiles')
            destination = open(os.path.join(dir, myFile.name), 'wb+')
            for chunk in myFile.chunks():
                destination.write(chunk)
            destination.close()
        return HttpResponse('ok')

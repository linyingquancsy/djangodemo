from django.shortcuts import render
from django.http import HttpResponse
import datetime

context = {'texts':[]}

def demo_01(request):
    print(request.method)
    if request.method == 'POST':
        speak = request.POST.get('speak',0)
        answer = request.POST.get('answer',0)
        addtext(context,speak,answer)
    return render(request, 'index.html', context=context)

def addtext(context,result,speech):
    context['texts'].append({"speak": result, "answer": speech})
    return context
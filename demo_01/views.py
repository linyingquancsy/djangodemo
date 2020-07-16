from django.shortcuts import render
from django.http import HttpResponse
import datetime

context = {
    'texts':[],
    'result':"今天天气真不错！"
}

def demo_01(request):
    '''
    获取树莓派上传的数据，3个一循环
    :param request:
    :return:
    '''
    print(request.method)
    if request.method == 'POST':
        speak = request.POST.get('speak',0)
        addtext(context,speak)
        print("len:",len(context['texts']))
        if len(context['texts'])>3:
            del context['texts'][0]
    return render(request, 'demo_02.html', context=context)

def addtext(context,result):
    context['texts'].append(result)
    return context
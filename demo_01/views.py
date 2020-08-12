from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import os
import time
from django.views.generic.base import View

# age=  1：表示首页，  2：表示语音，  3：表示手势

context = {
    'texts':[],
    'age': 0
}
result = {
    'texts':[],
    'age': 0
}
url = {
    'age': '*'
}

class index(View):
    '''
    首页
    '''
    def get(self, request):
        return render(request, "index.html", context=url)
    def post(self, request):
        print("post&&&&&&&&&&&&&&&&&&&&&&&")
        if request.POST.get("data") == "v":
            print("###########", url['age'])
            url['age'] = 2
            context['age'] = 0
            result['age'] = 0
        elif request.POST.get("data") == "g":
            url['age'] = 3
            context['age'] = 0
            result['age'] = 0

class voice(View):
    '''
    语音识别
    '''
    def get(self, request):
        return render(request, 'demo_02.html', context=context)
    def post(self, request):
        speak = request.POST.get('speak', 0)
        addtext(context, speak)
        print("len:", len(context['texts']))
        if len(context['texts']) > 3:
            del context['texts'][0]
        if request.POST.get("data") == 'break':
            print("返回首页")
            context['age'] = 1
            url['age'] = 0
            result['age'] = 0
        elif request.POST.get("data") == 'g':
            print("跳转手势")
            context['age'] = 3
            url['age'] = 0
            result['age'] = 0

class gesture(View):
    '''
    手势识别
    '''
    def get(self, request):
        return render(request, 'demo_01.html', context=result)
    def post(self, request):
        ges = request.POST.get('gesture', 0)
        print("######", ges)
        result['texts'].append(ges)
        if len(result['texts']) > 3:
            del result['texts'][0]
        if request.POST.get("data") == 'break':
            print("返回首页")
            result['age'] = 1
            context['age'] = 0
            url['age'] = 0
        elif request.POST.get("data") == 'v':
            print("跳转语音")
            result['age'] = 2
            context['age'] = 0
            url['age'] = 0

def addtext(context,result):
    context['texts'].append(result)
    return context



def get_user_profiles(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("0001.mp4", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("G:\\upload",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")
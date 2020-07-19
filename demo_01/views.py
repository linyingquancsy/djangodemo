from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

context = {
    'texts':[]
}
result = {
    'texts':[]
}

def index(request):
    return render(request, 'index.html')

def demo_01(request):
    '''
    手势识别
    :param request:
    :return:
    '''
    if request.method == 'POST':
        ges = request.POST.get('gesture',0)
        print("######",ges)
        result['texts'].append(ges)
        if len(result['texts'])>3:
            del result['texts'][0]
    return render(request, 'demo_01.html', context=result)


def demo_02(request):
    '''
    语音识别
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
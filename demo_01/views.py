from django.shortcuts import render
from django.http import HttpResponse
import time
import speech_recognition as sr
from ais_cli import tuling123

tuling_user_id = '421096'
tuling_api_key = '1f55700b32a14243a6ea696b1423d511'
snowboy_location = '/home/pi/voice_assistant/sb/'
snowboy_models = ['/home/pi/voice_assistant/sb/models/snowboy.umdl']
snowboy_config = (snowboy_location, snowboy_models)

import sys
sys.path.append(snowboy_location)
import snowboydecoder
sys.path.pop()

r = sr.Recognizer()
tuling = tuling123(user_id=tuling_user_id, api_key=tuling_api_key)

def demo_01(request):
    context = {
        'texts':[
            {
                "speak":"#",
                "answer":"$"
            }
        ]
    }

    with sr.Microphone(sample_rate=16000) as source:
        try:
            print("开始监听……")
            audio = r.listen(source,
                             phrase_time_limit=6,
                             snowboy_configuration=snowboy_config,
                             hot_word_callback=snowboydecoder.play_audio_file
                             )

            print("开始识别……")
            snowboydecoder.play_audio_file(fname=snowboy_location + 'resources/dong.wav')
            result = r.recognize_google_cn(audio, language='zh-CN')
        except sr.UnknownValueError:
            result = ''
        except Exception as e:
            print("识别错误：{0}".format(e))
        print("识别结果：" + result)

        try:
            speech = tuling.command(result)
            print(speech)
        except Exception as e:
            print("通讯失败：{0}".format(e))

    addtext(context,result,speech)

    return render(request, 'index.html', context=context)

def addtext(context,result,speech):
    context['texts'].append({"speak": result, "answer": speech})
    return context

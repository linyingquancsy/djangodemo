# import requests
# import time

# r = requests.get('http://127.0.0.1:8000/?data=v')
# res = requests.post('http://127.0.0.1:8000', data={'data': "v"})
# res = requests.post('http://127.0.0.1:8000/voice', data={'data': "break"})
# while True:
#     time.sleep(1)
#     res = requests.post('http://127.0.0.1:8000', data={'data': "v"})
# ges = requests.post('http://127.0.0.1:8000/gesture/', data={'gesture': "7"})
# ges = requests.post('http://127.0.0.1:8000/video/', data={'0001.mp4': 0})
# res = requests.post('http://127.0.0.1:8000/voice/', data={'speak': "阿萨的菜市场的"})
# res = requests.post('http://127.0.0.1:8000/voice/', data={'data': "break"})
# res = requests.post('http://127.0.0.1:8000/gesture/', data={'data': "break"})
# res = requests.post('http://127.0.0.1:8000/gesture/', data={'gesture': "阿萨的菜市场的"})
# print(res.text)

# 首页
# res = requests.post('http://127.0.0.1:8000/voice/', data={'data': "break"})
# res = requests.post('http://127.0.0.1:8000/voice/', data={'data': "g"})
# res = requests.post('http://127.0.0.1:8000/gesture/', data={'data': "break"})
# res = requests.post('http://127.0.0.1:8000/gesture/', data={'data': "v"})
# 语音
# res = requests.post('http://127.0.0.1:8000', data={'data': "v"})
# 手势
# res = requests.post('http://127.0.0.1:8000', data={'data': "g"})

# 首页
# res = requests.post('http://118.89.241.50:8000/voice/', data={'data': "break"})
# res = requests.post('http://118.89.241.50:8000/voice/', data={'data': "g"})
# res = requests.post('http://118.89.241.50:8000/gesture/', data={'data': "break"})
# res = requests.post('http://118.89.241.50:8000/gesture/', data={'data': "v"})
# 语音
# res = requests.post('http://118.89.241.50:8000', data={'data': "v"})
# 手势
# res = requests.post('http://118.89.241.50:8000', data={'data': "g"})

# import requests
# import json
# import unittest
#
#
# class UploadTest(unittest.TestCase):
#     """
#     请求上传视频的接口
#     """
#     def test_upload(self):
#         """
#         test case
#         :return:
#         """
#         url = 'http://127.0.0.1:8000/video/'
#         jsonrpc = "{\"title\": \"标题yzc0116\", \"tag\":\"标签yzc0116\",\"desc\":\"描述yzc0116\"}"
#         filepath = 'C:\\Users\lin\\Desktop\\python_cs\\django_1_1\\0001.mp4'
#         # 打开文件
#         fo = open(filepath, 'rb')
#         # video表示实际的文件参数
#         video = {'0001': fo}
#         # params表示实际的参数列表，包括：writetoken和JSONRPC这两个参数
#         params = {'writetoken': '7043f898-8322-4e39-8bb5-7956bf0eb641', 'JSONRPC': jsonrpc}
#         response = requests.post(url, data=params, files=video)
#         print("###@@@",response.text)
#         # self.assertEqual("{\"error\":\"0\"}", response.text)
#         # entity = json.loads(response.text)
#         # self.assertEqual(0, int(entity['error']))
#         # 关闭文件
#         fo.close()
#
# a = UploadTest()
# a.test_upload()


# import time
# import RPi.GPIO as GPIO
# import requests
#
# ip = '118.89.241.50:8000'
#
# # gpio13——对应按键数字1
# GPIO.setmode(GPIO.BCM)
# gpio_num13 = 13
# GPIO.setup(gpio_num13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# # gpio19——对应按键数字2
# GPIO.setmode(GPIO.BCM)
# gpio_num19 = 19
# GPIO.setup(gpio_num19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# # gpio26——对应按键数字3
# GPIO.setmode(GPIO.BCM)
# gpio_num26 = 26
# GPIO.setup(gpio_num26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
# def anjian_demo():
#     while True:
#         try:
#             if GPIO.input(gpio_num13) == 0:
#                 time.sleep(0.1)
#                 print("1被按下")
#                 res = requests.post('http://'+ip+'/gesture/', data={'data': "break"})
#                 res = requests.post('http://'+ip+'/voice/', data={'data': "break"})
#             elif GPIO.input(gpio_num19) == 0:
#                 time.sleep(0.1)
#                 print("2被按下")
#                 res = requests.post('http://'+ip, data={'data': "v"})
#                 res = requests.post('http://'+ip+'/gesture/', data={'data': "v"})
#             elif GPIO.input(gpio_num26) == 0:
#                 time.sleep(0.1)
#                 print("3被按下")
#                 res = requests.post('http://'+ip, data={'data': "g"})
#                 res = requests.post('http://'+ip+'/voice/', data={'data': "g"})
#         except:
#             print("按键错误")
#             break
#
# anjian_demo()




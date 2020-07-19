import requests

# res = requests.post('http://127.0.0.1:8000/voice/', data={'speak': "9"})
# ges = requests.post('http://127.0.0.1:8000/gesture/', data={'gesture': "7"})
# ges = requests.post('http://127.0.0.1:8000/video/', data={'0001.mp4': 0})
# res = requests.post('http://118.89.241.50:8000', data={'speak': "阿萨的菜市场的"})
# print(res.text)


import requests
import json
import unittest


class UploadTest(unittest.TestCase):
    """
    请求上传视频的接口
    """
    def test_upload(self):
        """
        test case
        :return:
        """
        url = 'http://127.0.0.1:8000/video/'
        jsonrpc = "{\"title\": \"标题yzc0116\", \"tag\":\"标签yzc0116\",\"desc\":\"描述yzc0116\"}"
        filepath = 'C:\\Users\lin\\Desktop\\python_cs\\django_1_1\\0001.mp4'
        # 打开文件
        fo = open(filepath, 'rb')
        # video表示实际的文件参数
        video = {'0001': fo}
        # params表示实际的参数列表，包括：writetoken和JSONRPC这两个参数
        params = {'writetoken': '7043f898-8322-4e39-8bb5-7956bf0eb641', 'JSONRPC': jsonrpc}
        response = requests.post(url, data=params, files=video)
        print("###@@@",response.text)
        # self.assertEqual("{\"error\":\"0\"}", response.text)
        # entity = json.loads(response.text)
        # self.assertEqual(0, int(entity['error']))
        # 关闭文件
        fo.close()

a = UploadTest()
a.test_upload()
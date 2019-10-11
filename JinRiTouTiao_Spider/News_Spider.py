import hashlib
import json
import time
import requests
import execjs



class JinRiTouT():

    def __init__(self):
        self.requests = requests
        self.headers =  {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'tt_webid=6730750239051843075; csrftoken=d19c67d5c5c53f5073b57588f47ef202; W2atIF=1; _ga=GA1.2.999591731.1567135973; _gid=GA1.2.262157934.1567135973; __tasessionId=ftgrwnstk1567135991821',
    'Host':'m.toutiao.com',
    'Referer':'https://m.toutiao.com/?channel=__all__',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    }

    # 获取url中的参数
    def get_signature(self):
        with open("./get_as_cp_signature.js","r") as f:
            ctx = execjs.compile(f.read())
            param = ctx.call("get_as_cp_signature")
            param = json.loads(param)
            as_str = param["as"]
            cp_str = param["cp"]
            _signature = param["_signature"]
            return as_str,cp_str,_signature

    # 获取内容
    def get_news(self,as_str,cp_str,behot_time,_signature):
        url = "https://m.toutiao.com/list/?tag=__all__&ac=wap&count=20&format=json_raw&as={}&cp={}&max_behot_time={}&_signature={}".format(as_str,cp_str,behot_time,_signature)
        #
        requests = self.requests.session()
        response = requests.get(url,headers = self.headers)
        html = response.content
        html = json.loads(html)
        behot_time = html["data"][0]["behot_time"]
        return html,behot_time

    # 保存内容
    def save_news(self,html):
        with open("./new.txt", "a", encoding="utf-8") as f:
            json.dump(html, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    behot_time = 0
    for i in range(100):
        news = JinRiTouT()
        as_str,cp_str,_signature = news.get_signature()
        html,behot_time1 = news.get_news(as_str,cp_str,behot_time,_signature)
        behot_time = behot_time1
        news.save_news(html)
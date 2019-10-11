import json
import random
import requests
from requests.exceptions import RequestException
from lxml import etree
from multiprocessing import Pool

def get_one_page(url):
    ua = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"]

    headers = {
        "User-Agent":random.choice(ua)
    }
    try:
        response = requests.get(url,headers= headers)
        if response.status_code == 200:
            html = response.content.decode()
            return html
        return None
    except RequestException:
        return None

def parse_one_page(html):
    html = etree.HTML(html)
    dd_list  = html.xpath("//dl[@class='board-wrapper']/dd")
    movie_list = []
    for dd in dd_list:
        item = {}
        item["index"] = dd.xpath("./i/text()")[0]
        item["movie_name"] = dd.xpath(".//p[@class='name']/a/text()")[0]
        item["scores"] = dd.xpath(".//p[@class='score']//text()")[0]+dd.xpath(".//p[@class='score']//text()")[1]
        item["actor"] = dd.xpath(".//p[@class='star']/text()")[0].strip()
        item["creat_time"] = dd.xpath(".//p[@class='releasetime']/text()")[0].split("：")[1]
        item["img_href"] = dd.xpath(".//img[@class='board-img']/@data-src")[0].split("@")[0]
        movie_list.append(item)
    with open("MaoYan_100.txt","a",encoding="utf-8") as f:
        json.dump(movie_list,f,indent=4,ensure_ascii=False)

    print(movie_list)


def run(page):
    url = "https://maoyan.com/board/4?offset={}"
    url = url.format(page)
    html = get_one_page(url)
    parse_one_page(html)

if __name__ == '__main__':
    pool = Pool()
    pool.map(run,[i * 10 for i in range(10)])




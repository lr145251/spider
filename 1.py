# import requests
# from lxml import etree
# import csv
# import pandas as pd
#
#
#
# url = "https://www.baidu.com"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#     "Cookie":"BIDUPSID=C9060F39DC7F8D859A1B95B6C56D6D9F; PSTM=1553741258; BD_UPN=12314753; BAIDUID=E9A234C2087AECADBF23E68514C7FCD3:FG=1; __cfduid=d92acb53783ec015ff5e1a7923c9b10361560161087; MSA_WH=375_812; H_WISE_SIDS=130985_125704_135752_113879_128069_120172_132911_131246_130763_132378_131518_118889_118874_118853_118825_118789_107311_133351_135484_132553_129656_132250_124637_134854_128968_135308_133838_133847_132551_135873_134046_134751_129645_131423_134601_133683_133539_110085_134149_134153_127969_131753_131951_135671_135459_127416_135045_135038_134934_135006_134383_135503_134725_134350; COOKIE_SESSION=3020_0_9_7_73_71_0_6_9_6_0_0_26830_0_1_0_1569406936_0_1569406935%7C9%234962_33_1568710629%7C9; delPer=0; H_PS_PSSID=1465_21093_29523_29721_29567_29221_26350_22158; BDUSS=HU3U2FzME9jQUVUUzRwZElhSjR-RWdhRFBhRVRTRTlwNDdrNUc4blFQWGhJcmhkRVFBQUFBJCQAAAAAAAAAAAEAAACCWdsytLq9v7XEwbpaaGlNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOGVkF3hlZBda; BD_HOME=1; sugstore=1"
# }
# resp = requests.get(url,headers=headers)
#
# html_text = etree.HTML(resp.content)
#
# li_list = html_text.xpath("//ul[@class='s-news-rank-content']/li")
#
# title = []
# href = []
# for li in li_list:
#     # print(type(li.xpath(".//a/text()")[0]))
#     title.append(li.xpath(".//a/text()")[0])
#
#     href.append(li.xpath(".//a/@href")[0])
#
# df = pd.DataFrame({"标题":title,"连接":href})
# df.to_csv("baidu.csv",index=False,sep=",")
# baidu = pd.read_csv("baidu.csv")
# print(baidu)
# import random
#
# from matplotlib import pyplot as plt
#
# nums = []
# for i in range(0, 1001):
#     num = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
#     nums.append(num)
#
# plt.figure(figsize=(20, 8))
# bins = 3
# group = 18
# plt.hist(nums,group)
# plt.show()

# list1 = ["a","b"]
#
# list1.pop("a")
# print(list1)


# 定时任务

# 添加应用
INSTALLED_APPS = [
    'django_crontab',  # 定时任务
]
# 定时任务
CRONJOBS = [
    # 每5分钟执行一次生成主页静态文件
    ('*/5 * * * *', 'contents.crons.generate_static_index_html', '>> /Users/delron/Desktop/meiduo_mall/logs/crontab.log')
]
# 解决crontab中文问题
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'
# 添加定时任务到系统中
python manage.py crontab add
# 显示已激活的定时任务
python manage.py crontab show
# 移除定时任务
python manage.py crontab remove
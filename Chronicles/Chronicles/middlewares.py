# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals


class Chronicles():

    def process_request(self, request, spider):

        request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        cookies = {"clientId":"CID88843726f6a0d90f4f304afc03644189", "JSESSIONID":"2264433632901ABF4E95AE5DCE7AEE1A"}

        request.cookies = cookies

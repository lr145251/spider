# -*- coding: utf-8 -*-
from copy import deepcopy

import scrapy


class ChroniclesSpider(scrapy.Spider):
    name = 'chronicles'
    allowed_domains = ['61.175.198.136']
    start_urls = ['http://61.175.198.136:8083/rwt/243/http/GEZC6MJZFZZUPLSSGMZUVPBRHA6A/C/LocalChronicle.aspx']

    # 拿到所有的省份
    def parse(self, response):
        # 拿到所有省份的li标签,里面包含各个省份的url
        li_list= response.xpath("//ul[@class='conference_ul']/li")
        for li in li_list[0:1]:
            item = {}
            item["pro_name"]= li.xpath(".//t/text()").extract_first()
            item["b_url"] = li.xpath("./a/@href").extract_first()
            yield response.follow(item["b_url"],callback=self.parse_list,meta={"item":deepcopy(item)})
        # print(item)


    # 省份下所有的方志
    def parse_list(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//ul[@class='local_items']/li")
        for li in li_list[0:1]:
            item["records_name"] = item["pro_name"] +"-"+ li.xpath(".//t/text()").extract_first()
            item["r_url"] = li.xpath("./a/@href").extract_first()
            yield response.follow(item["r_url"],callback=self.parse_detail,meta={"item":deepcopy(item)})


    # 方志拿到下载pdf的连接
    def parse_detail(self,response):

        item = response.meta["item"]
        # 一级
        li_list = response.xpath("//ul[@class='localchr_ul']/li[@class='']/a[@class='pdf_img']/..")
        for li in li_list:
            item["f_file_name"] = item["records_name"] +"-"+li.xpath(".//t/text()").extract_first()
            item["f_file_url"] = li.xpath("./a[@class='pdf_img']/@href").extract_first()
            yield response.follow(item["f_file_url"],callback=self.parse_file,meta={"item":deepcopy(item)})

        # 二级
        inner_li_list = response.xpath("//ul[@class='localchr_ul']/li[@class='padchapter']/a[@class='pdf_img']/..")
        for li in inner_li_list:
            up_name = li.xpath("//ul[@class='localchr_ul']/li[@class='padchapter']/preceding-sibling::li[@class=''][1]//t/text()").extract_first()
            item["t_file_name"] = item["records_name"] +"_"+ up_name +"_"+li.xpath(".//t/text()").extract_first()
            item["t_file_url"] = li.xpath("./a[@class='pdf_img']/@href").extract_first()

            yield response.follow(item["t_file_url"],callback=self.parse_inner_file,meta={"item":deepcopy(item)})


    # 拿到第二层数据
    def parse_inner_file(self,response):
        item = response.meta["item"]
        rel_url = response.xpath("//a[@id='doDownload']/@href").extract_first()
        yield response.follow(rel_url, callback=self.parse_inner_rel_file, meta={"item": deepcopy(item)})

    # 拿到下载的连接 有重定向
    def parse_file(self,response):
        item = response.meta["item"]
        # print(response)

        relu_url = response.xpath("//a[@id='doDownload']/@href").extract_first()
        yield response.follow(relu_url,callback=self.parse_rel_file,meta={"item":item})
        # print(response.text)

    # 真正的文件下载和保存
    def parse_rel_file(self,response):
        item = response.meta["item"]
        # print(item)
        file_name = item["f_file_name"]

        with open("{}.pdf".format(file_name),"wb") as f:
            f.write(response.body)
        # print(response.body)
    def parse_inner_rel_file(self,response):
        item = response.meta["item"]
        print(item)
        file_name = item["t_file_name"]

        with open("{}.pdf".format(file_name),"wb") as f:
            f.write(response.body)
        # print(response.body)
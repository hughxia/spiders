# -*- coding: utf-8 -*-
import scrapy

import re
import json
import time


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']

    # 京东手机分类
    start_urls = ["https://list.jd.com/list.html?cat=9987,653,655"]

    def parse(self, response):
        # url: https://list.jd.com/list.html?cat=9987,653,655&page=2
        try:
            current_page = int(re.findall("page=(.*?)&", response.url)[0])
        except:
            current_page = 1

        try:
            total_page = int(response.css("#J_topPage > span > i::text").extract()[0])
        except:
            total_page = 1

        # xpath 写法
        # product_ids = response.xpath("//li[@class='gl-item']/div/@data-sku").extract()
        product_ids = response.css(".gl-item > div::attr(data-sku)").extract()
        if product_ids:
            for product_id in product_ids:
                comment_url = f"https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1826&productId={product_id}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
                yield scrapy.Request(url=comment_url, callback=self.comment_parse, dont_filter=True)
        else:
            print("获取商品id失败")

        # while int(current_page) <= int(total_page):
        #     current_page 

    def comment_parse(self, response):
        # Request URL: https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1826&productId=100004049987&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1

        current_page = int(re.findall(r"page=(.*?)&", response.url)[0])
        data = re.findall(r"\((.*?)\);", response.body.decode("gbk"))
        if data:
            json_data = json.loads(data[0])
            comments = json_data["comments"]
            max_page = json_data["maxPage"]

            for comment in comments:
                yield comment
            
            if int(max_page) > int(current_page)+1:
                new_page = current_page + 1
                new_url = response.url.replace(str(current_page), str(new_page))
                yield scrapy.Request(url=new_url, callback=self.comment_parse, dont_filter=True)

        else:
            print(f"获取评论失败:{response.url}")

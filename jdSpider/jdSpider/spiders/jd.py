# -*- coding: utf-8 -*-
import scrapy

import re


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://item.jd.com/100005981268.html']

    def parse(self, response):
        for url in self.start_urls:
            product_id = re.findall(r"com/(.*?).html", url)[0]
            print("product_id:", product_id)
            pass

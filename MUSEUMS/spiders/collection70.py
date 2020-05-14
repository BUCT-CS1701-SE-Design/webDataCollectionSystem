# -*- coding: utf-8 -*-
import scrapy


class Collection70Spider(scrapy.Spider):
    name = 'collection70'
    allowed_domains = ['jiawuzhanzheng.org']
    start_urls = ['http://jiawuzhanzheng.org/']

    def parse(self, response):
        pass

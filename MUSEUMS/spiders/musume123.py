# -*- coding: utf-8 -*-
import os
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume123Spider(scrapy.Spider):
    name = 'musume123'
    allowed_domains = ['gansumuseum.com']
    start_urls = ['http://www.gansumuseum.com/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=123
        item["museumName"] ='甘肃省博物馆'
        item["Location"] ='甘肃省兰州市七里河区西津西路3'
        #item["Location"] = str(item["Location"]).replace(u'\\xa0', u' ')
        #item["Location"] = str(item["Location"]).replace(u'\xa0', u' ')
        item["Link"]='http://www.gansumuseum.com/'
        item["opentime"] = response.xpath('/html/body/div[1]/div[1]/div[2]/div/ul/li[3]/text()').extract_first()
        item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u' ')
        item["opentime"] = str(item["opentime"]).replace(u'\xa0', u' ')
        item["telephone"]='0931-2346308'
        #item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u' ')
        #item["telephone"] = str(item["telephone"]).replace(u'\xa0', u' ')
        url='http://www.gansumuseum.com/about/show-1.html'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"] = response.xpath('normalize-space(/html/body/div/div[2]/div/div[2]/div[2]/ul/li[1]/div[1]/p/span/text())').extract_first()
        item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 

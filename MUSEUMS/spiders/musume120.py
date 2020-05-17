# -*- coding: utf-8 -*-
import os
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume120Spider(scrapy.Spider):
    name = 'musume120'
    allowed_domains = ['xabwy.com']
    start_urls = ['http://www.xabwy.com/index.aspx']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=120
        item["museumName"] ='西安博物院'
        item["Location"] ='陕西省西安市南门外友谊西路'
        #item["Location"] = str(item["Location"]).replace(u'\\xa0', u' ')
        #item["Location"] = str(item["Location"]).replace(u'\xa0', u' ')
        item["Link"]='http://www.xabwy.com'
        item["opentime"] = response.xpath('normalize-space(/html//div[4]/div[2]/div[2]/text()[1])').extract_first()
        item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u' ')
        item["opentime"] = str(item["opentime"]).replace(u'\xa0', u' ')
        item["telephone"]=response.xpath('normalize-space(/html//div[4]/div[2]/div[2]/text()[2])').extract_first()
        item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u' ')
        item["telephone"] = str(item["telephone"]).replace(u'\xa0', u' ')
        url='http://www.xabwy.com/Statics/2020.01/66.html'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"] = response.xpath('normalize-space(/html//div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/p[1]/text())').extract_first()
        item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 

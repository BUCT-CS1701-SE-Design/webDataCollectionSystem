# -*- coding: utf-8 -*-
import os
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume127Spider(scrapy.Spider):
    name = 'musume127'
    allowed_domains = ['nxbwg.com']
    start_urls = ['https://www.nxbwg.com/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=127
        item["museumName"] ='宁夏回族自治区博物馆'
        item["Location"] =response.xpath('normalize-space(/html//footer/div/div[2]/div/div[1]/span[3])').extract_first()
        item["Location"] = str(item["Location"]).replace(u'\\xa0', u' ')
        item["Location"] = str(item["Location"]).replace(u'\xa0', u' ')
        item["Link"]='https://www.nxbwg.com/'
        item["opentime"] = '周一闭馆,周二-周日:9:00-16:50'
        #item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u' ')
        #item["opentime"] = str(item["opentime"]).replace(u'\xa0', u' ')
        item["telephone"]='电话：(0951)5085093'
        #item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u' ')
        #item["telephone"] = str(item["telephone"]).replace(u'\xa0', u' ')
        url='https://www.nxbwg.com/a/30.html'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"] = response.xpath('normalize-space(/html//div[1]/div/main/div/div[2]/div[2]/p[2]/text())').extract_first()
        item["introduction"] = str(item["introduction"]).replace(u'\u2003', u' ')
        item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 

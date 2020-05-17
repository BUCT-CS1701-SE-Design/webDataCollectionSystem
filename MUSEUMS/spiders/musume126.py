# -*- coding: utf-8 -*-
import os
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume126Spider(scrapy.Spider):
    name = 'musume126'
    allowed_domains = ['nxgybwg.com']
    start_urls = ['http://www.nxgybwg.com/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=126
        item["museumName"] ='宁夏固原博物馆'
        item["Location"] = response.xpath('normalize-space(/html//div[3]/div/div[2]/p[2]/text())').extract_first()
        item["Location"] = str(item["Location"]).replace(u'\\xa0', u'')
        item["Location"] = str(item["Location"]).replace(u'\xa0', u'')
        item["Link"]='http://www.nxgybwg.com/'
        item["opentime"] = response.xpath('normalize-space(/html//div[2]/div/div[7]/div/div/div[1]/div/div[1]/p/text()[2])').extract_first()
        item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u'')
        item["opentime"] = str(item["opentime"]).replace(u'\xa0', u'')
        item["telephone"]=response.xpath('normalize-space(/html//div[3]/div/div[2]/p[3]/text())').extract_first()
        item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u'')
        item["telephone"] = str(item["telephone"]).replace(u'\xa0', u'')
        url='http://www.nxgybwg.com/e/action/ShowInfo.php?classid=1&id=307'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"] = response.xpath('/html//div[2]/div/div[2]/div[2]/div/div[2]/div/p/text()').extract_first()
        item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        item["introduction"] = str(item["introduction"]).replace(u'\u3000', u' ')
        item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 

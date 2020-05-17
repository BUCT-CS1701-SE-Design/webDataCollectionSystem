# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置




class Musume117Spider(scrapy.Spider):
    name = 'musume117'
    allowed_domains = ['hylae.com']
    start_urls = ['http://www.hylae.com/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=117
        item["museumName"]='汉阳陵博物馆'
        item["Location"]='地址：西安咸阳国际机场专线公路东段'
        item["Link"]='http://www.hylae.com/'
        item["opentime"]=response.xpath("normalize-space(/html/body/div[3]/div[2]/div[2]/div/div[1]/div[2]/text()[1])").extract_first()
        item["telephone"]='029-62657569'
        url='http://www.hylae.com/index.php?ac=article&at=list&tid=10'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]

        item["introduction"]=response.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/p/text()").extract()
        item["introduction"]=str(item["introduction"]).replace(u'\xa0', u' ')
        item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')


        #print(item)
        yield item 

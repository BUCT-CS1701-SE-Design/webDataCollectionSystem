# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume108Spider(scrapy.Spider):
    name = 'musume108'
    allowed_domains = ['ynmuseum.org']
    start_urls = ['http://www.ynmuseum.org']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=108
        item["museumName"]='云南省博物馆'
        item["Location"]='云南省昆明市广福路6393号'
        item["Link"]='http://www.ynmuse um.org'
        item["opentime"]=response.xpath("/html/body/div/div[3]/div[2]/div/div[1]/div/div[3]/div/text()").extract_first()
        item["telephone"]=response.xpath("/html//div/div[3]/div[2]/div/div[1]/div/div[3]/div/text()").extract_first()
        url='http://www.ynmuseum.org'+response.xpath("//div/div[1]/div/ul/li/div/div/div/a/@href").extract_first()
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]=response.xpath("/html/body/div/div[3]/div[1]/div[2]/div/div[1]/div/div//div[@class='p']/text()").extract()
        #print(item)
        yield item

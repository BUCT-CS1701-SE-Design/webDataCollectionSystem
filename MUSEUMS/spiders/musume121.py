    # -*- coding: utf-8 -*-
import os
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume121Spider(scrapy.Spider):
    name = 'musume121'
    allowed_domains = ['bjqtm.com']
    start_urls = ['http://www.bjqtm.com/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=121
        item["museumName"] ='宝鸡青铜器博物院'
        item["Location"] =response.xpath('normalize-space(/html/body/div[3]/div/div[2]/text()[4])').extract_first()
        item["Location"] = str(item["Location"]).replace(u'\\xa0', u' ')
        item["Location"] = str(item["Location"]).replace(u'\xa0', u' ')
        item["Link"]='http://www.bjqtm.com/'
        item["opentime"] = response.xpath('/html/body/div[1]/div[2]/div[1]/p[1]/text()[1]').extract_first()
        #item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u' ')
        #item["opentime"] = str(item["opentime"]).replace(u'\xa0', u' ')
        item["telephone"]=response.xpath('normalize-space(/html/body/div[1]/div[2]/div[1]/p[2])').extract_first()
        item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u' ')
        item["telephone"] = str(item["telephone"]).replace(u'\xa0', u' ')
        url='http://www.bjqtm.com/index.php?ac=article&at=list&tid=44'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"] = response.xpath('/html/body/div[1]/div/div[2]/div[3]/div/div/p/text()').extract()
        #item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        #item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 

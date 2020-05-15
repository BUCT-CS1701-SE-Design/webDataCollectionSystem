# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item


class Collection71Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }

    name = 'collection71'
    allowed_domains = ['bowuguan.qingzhou.gov.cn']
    start_urls = ['http://bowuguan.qingzhou.gov.cn/cp/lxs/']
    
    def parse(self, response):
        td_list=response.xpath("/html/body/div[3]/table/tbody/tr/td/table/tbody/tr[2]/td")
        for td in td_list:
            item=collection75Item()
            item["museumID"]=71
            item["collectionImage"]='http://bowuguan.qingzhou.gov.cn/cp/lxs/'+td.xpath("./table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img/@src").extract_first()
            item["collectionName"]=td.xpath("./table/tbody/tr/td/table/tbody/tr[2]/td/a/span/text()").extract_first()
            url='http://bowuguan.qingzhou.gov.cn/cp/lxs/'+td.xpath("./table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item}
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["collectionIntroduction"]=response.xpath("/html/body/div[2]/table/tbody/tr[4]/td/div/p[4]/font/span/font/font/text()").extract_first()
        if response.xpath("/html/body/div[2]/table/tbody/tr[4]/td/div/p[4]/font/span/font/font/text()").extract_first() is None:
            item["collectionIntroduction"]=response.xpath("/html/body/div[2]/table/tbody/tr[4]/td/div/p[4]/font/span/font/text()").extract_first()
        
        yield item
        ''''area_list=response.xpath("//map[@name='Map']/area")
        for a in area_list:
            global url
            url ='http://bowuguan.qingzhou.gov.cn/cp/'+a.xpath("./@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
            )
    def parse_detail(self,response):
        item=collection75Item()
        item["museumID"]=71
        item["collectionImage"]=response.xpath("/html/body/div[3]/table/tbody/tr/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/a/img/@src").extract_first()
        print(item)
        #tr_list=response.xpath("/html/body/div[3]/table/tbody/tr/td/table/tbody/tr")'''
        '''for tr in tr_list:
            td_list=tr.xpath("./td")
            for td in td_list:
                #item=collection75Item()
                #item["museumID"]=71
               # item["collectionImage"]=td.xpath("./table/tbody/tr[2]/td[1]/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img/@src").extract_first()
                item["collectionName"]=td.xpath("./table/tbody/tr[2]/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/a/span/text()").extract_first()
                url1=td.xpath("./table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/@href").extract_first()
                if url1 is not None:
                    global url2
                    url2=url+url1
                    yield scrapy.Request(
                url2,
                callback=self.parse_detail2,
                meta={"item":item},
            )
    def parse_detail2(self,response):
        item=response.meta["item"]
        item["collectionIntroduction"]=response.xpath("/html/body/div[2]/table/tbody/tr[4]/td/div/p[2]/span/text()").extract()
        print(item)'''


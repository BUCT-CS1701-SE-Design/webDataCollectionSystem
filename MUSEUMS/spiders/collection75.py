# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import collection75Item

class Collection75Spider(scrapy.Spider):
    name = 'collection75'
    allowed_domains = ['chnmus.net']
    start_urls = ['http://www.chnmus.net/sitesources/hnsbwy/page_pc/dzjp/zpjc/list1.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    def parse(self, response):
        
        d_list=response.xpath("//div[@class='view2']/div[@class='collect-box']")       
        for d in d_list:
            dy=d.xpath("./div/div[@class='collect-info']")
            i=0
            for dd in dy:
                item=collection75Item()
                item["museumID"]=75
                i+=1
                if i>3:
                    break
                else:
                    item["collectionImage"]='http://www.chnmus.net'+dd.xpath("./a/img/@src").extract_first()
                    item["collectionName"]=dd.xpath("./a/h5/text()").extract_first()
                    url='http://www.chnmus.net'+dd.xpath("./a/@href").extract_first()               
                    
                 
                #处理详 情页
                    yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
                    
    def parse_detail(self,response):
        item=response.meta["item"]
        
        p_list=response.xpath("//div[@class='article-detail']/p")
        content=""
        for p in p_list:
            x=p.xpath("./text()").extract_first()
            if x != None:
                content+=x
                #break
        #print(content)
        item["collectionIntroduction"]=content
        yield item
        #yield item 


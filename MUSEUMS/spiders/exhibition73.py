# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }

class Exhibition73Spider(scrapy.Spider):
    name = 'exhibition73'
    allowed_domains = ['ytmuseum.com']
    start_urls = ['http://www.ytmuseum.com/zhanting/list.html']

    def parse(self, response):
        li_list=response.xpath("/html/body/div[3]/div[2]/div/div/div[4]/div/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=73
            item["exhibitionTheme"]=li.xpath("./div[2]/a/text()").extract_first()
            item["exhibition_picture"]='http://www.ytmuseum.com'+li.xpath("./div[1]/a/img/@src").extract_first()
            #print(item)
            url='http://www.ytmuseum.com'+li.xpath("./div[1]/a/@href").extract_first()
            #print(url)
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item}
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["exhibitionTime"]=''
        #item["exhibitionIntroduction"]=response.xpath("/html/body/div[3]/div[2]/div/div/div[4]/table/tr[3]/td/p[1]/text()").extract_first()
        item["exhibitionIntroduction"]=response.xpath("/html/body/div[3]/div[2]/div/div/div[4]/table/tr[3]/td/div[1]/div[2]/span/text()").extract_first()
        if item["exhibitionIntroduction"] is None:
            item["exhibitionIntroduction"]=response.xpath("/html/body/div[3]/div[2]/div/div/div[4]/table/tr[3]/td/p[1]/text()").extract_first()
        elif item["exhibitionIntroduction"] is None:
            item["exhibitionIntroduction"]=response.xpath("/html/body/div[3]/div[2]/div/div/div[4]/table/tr[3]/td/div[1]/div[1]/div[2]/span/text()").extract_first()
        elif item["exhibitionIntroduction"] is None:
            item["exhibitionIntroduction"]=response.xpath("/html/body/div[3]/div[2]/div/div/div[4]/table/tr[3]/td/div[1]/span/text()").extract_first()
        if item["exhibitionIntroduction"] is not None:
            item["exhibitionIntroduction"]= ''.join(item["exhibitionIntroduction"].split())
        
        yield item

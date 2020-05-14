# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }



class Collection64Spider(scrapy.Spider):
    name = 'collection64'
    allowed_domains = ['jgsgmbwg.com']
    start_urls = ['http://www.jgsgmbwg.com/bwgnews.php?cid=71']

    def parse(self, response):
        li_list=response.xpath("//div[@class='subCont']/ul[@class='news_list2']/li")
        for li in li_list:
            #print(li)
            item=collection75Item()
            item["museumID"]=64
            item["collectionName"]=li.xpath("./span[@class='title']/a/text()").extract_first()
            url='http://www.jgsgmbwg.com/'+li.xpath("./span[@class='title']/a/@href").extract_first()
            
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item},
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        if response.xpath("/html/body/div[1]/div[5]/div[2]/div/div[2]/p[1]/img/@src").extract_first() is not None:

            item["collectionImage"]='http://www.jgsgmbwg.com'+response.xpath("/html/body/div[1]/div[5]/div[2]/div/div[2]/p[1]/img/@src").extract_first()
        else:
            item["collectionImage"]=''
        item["collectionIntroduction"]=response.xpath("/html/body/div[1]/div[5]/div[2]/div/div[2]/p[3]/span/text()").extract_first()
        yield item
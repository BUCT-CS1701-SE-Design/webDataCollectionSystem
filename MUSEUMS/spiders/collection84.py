import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection84Spider(scrapy.Spider):
    name = 'collection84'
    allowed_domains = ['1911museum.com']
    start_urls = ['http://www.1911museum.com/Introduce/Details/zs_wwzc'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=84
        url1=response.xpath("//ul[@class='secondmenu']//li//@href").getall()
        for url in url1:
            if 'Collection' in url:
                url='http://www.1911museum.com'+url
                yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        a=0
        url2=response.xpath("//ul[@class='collectlist']/li/a[1]/@href").getall()
        for ur in url2:
            ur='http://www.1911museum.com'+ur
            a+=1
            if(a>5):
                break
            yield scrapy.Request(ur,callback=self.Info,meta={"item":item})
    def Info(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//div[@class='title']/text()").get()
        collectionIntroduction=response.xpath("//div[@class='cont']/p/span//text()").getall()
        collectionImage=response.xpath("//div[@class='cont']/p[1]/span/img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item
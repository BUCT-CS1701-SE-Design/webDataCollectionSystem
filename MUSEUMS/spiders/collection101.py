import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection101Spider(scrapy.Spider):
    name = 'collection101'
    allowed_domains = ['wuhouci.net.cn']
    start_urls = ['http://www.wuhouci.net.cn/cultrue-relic.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=101
        url1=response.xpath("//div[@id='subNav']//div[@class='r l5']/a/@href").getall()
        for url in url1:
            url='http://www.wuhouci.net.cn/'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        url1=response.xpath("//div[@class='crList']/a/@href").getall()
        for url in url1:
            url='http://www.wuhouci.net.cn/'+url
            yield scrapy.Request(url,callback=self.Info,meta={"item":item})
    def Info(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//div[@class='title']/text()").get().strip()
        collectionIntroduction=response.xpath("//div[@class='des']/text()").getall()
        collectionImage='http://www.wuhouci.net.cn/'+response.xpath("//div[@class='crWarpImg']/img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item
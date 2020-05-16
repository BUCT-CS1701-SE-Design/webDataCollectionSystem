import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection91Spider(scrapy.Spider):
    name = 'collection91'
    allowed_domains = ['gznywmuseum.org']
    start_urls = ['https://www.gznywmuseum.org/'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=91
        url1=response.xpath("//ul[@class='nav navbar-nav']/li[4]//li//@href").getall()
        for url in url1:
            url='https://www.gznywmuseum.org'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        url2=response.xpath("//div[@class='cz-list-content']/div//@href").getall()
        for ur in url2:
            ur='https://www.gznywmuseum.org'+ur
            yield scrapy.Request(ur,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//p[@class='cz-list-detail-view-info-title']/text()").get().strip()
        collectionIntroduction=response.xpath("//div[@class='cz-list-detail-view-info-content']/p//text()").getall()
        collectionImage='https://www.gznywmuseum.org'+response.xpath("//div[@class='zoompic']/img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item
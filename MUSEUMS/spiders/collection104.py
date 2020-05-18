import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection104Spider(scrapy.Spider):
    name = 'collection104'
    allowed_domains = ['scmuseum.cn']
    start_urls = ['http://www.scmuseum.cn/list-1657.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=104
        url1=response.xpath("//ul[@class='menu-sidebar']/li//@href").getall()
        for url in url1:
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        url1=response.xpath("//div[@id='portfolio']/div//@href").getall()
        for url in url1:
            yield scrapy.Request(url,callback=self.Info,meta={"item":item})
    def Info(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//*[@id='article-1']/h1/text()").get().strip()
        collectionIntroduction=response.xpath("//div[@id='MyContent']/p/text()").getall()
        collectionImage=response.xpath("//div[@id='MyContent']/p//@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item
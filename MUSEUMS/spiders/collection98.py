import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection98Spider(scrapy.Spider):
    name = 'collection98'
    allowed_domains = ['hainanmuseum.org']
    start_urls = ['http://www.hainanmuseum.org/gcjp/gcjp'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=98
        url1=response.xpath("//ul[@class='gmes fix']/li//@href").getall()
        for url in url1:
            url='http://www.hainanmuseum.org/'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//div[@class='left-show']/h1//text()").get().strip()
        collectionIntroduction=response.xpath("//div[@class='introduce']/p/text()").getall()
        collectionImage='http://www.hainanmuseum.org/'+response.xpath("//div[@class='show-box']/img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item
        
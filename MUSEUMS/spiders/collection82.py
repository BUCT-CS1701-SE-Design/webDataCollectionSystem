import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection82Spider(scrapy.Spider):
    name = 'collection82'
    allowed_domains = ['jzmsm.org']
    start_urls = ['http://www.jzmsm.org/yk/cangpin/'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=82
        url1=response.xpath("//ul[@class='xwdt']/li//@href").getall()
        for url in url1:
            url='http://www.jzmsm.org'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//div[@class='content']//h1/text()").get().strip()
        collectionIntroduction=response.xpath("//div[@class='content']/p[5]//text()").getall()
        collectionImage='http://www.jzmsm.org'+response.xpath("//div[@class='content']/p[3]/img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item
import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection87Spider(scrapy.Spider):
    name = 'collection87'
    allowed_domains = ['ssmzd.com']
    start_urls = ['http://www.ssmzd.com/jngwwjx/jngwwcl/Index.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=87
        url1=response.xpath("//div[@id='p_item']//div/a/@href").getall()
        for url in url1:
            url='http://www.ssmzd.com'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//*[@id='ArticleTit']/text()").get().strip()
        collectionIntroduction=response.xpath("//div[@id='conbox']//text()").getall()
        collectionImage='http://www.ssmzd'+response.xpath("//div[@id='PrintTxt']/center/img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item
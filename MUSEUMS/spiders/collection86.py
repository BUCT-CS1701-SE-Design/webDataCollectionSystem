import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection80Spider(scrapy.Spider):
    name = 'collection86'
    allowed_domains = ['hnmuseum.com']
    start_urls = ['http://61.187.53.122/list.aspx?lang=zh-CN']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=86
        url1=response.xpath("//ul[@id='thumbnailUL']/li//a/@href").getall()
        for url in url1:
            url='http://61.187.53.122/'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item},dont_filter=True)
    def Others(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//div[@class='title']/text()").get()
        collectionIntroduction=response.xpath("//div[@id='divContent']//text()").getall()
        collectionImage='http://61.187.53.122'+response.xpath("//*[@id='linkPicture']/img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item
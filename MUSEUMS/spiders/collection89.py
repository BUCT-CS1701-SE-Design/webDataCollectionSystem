import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection89Spider(scrapy.Spider):
    name = 'collection89'
    allowed_domains = ['chinajiandu.cn']
    start_urls = ['http://www.chinajiandu.cn/Collection/List/wj'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=89
        url1=response.xpath("//ul[@class='typelist normalfont']/li//@href").getall()
        for url in url1:
            url='http://www.chinajiandu.cn'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        url2=response.xpath("/html/body/div[3]/div/ul[2]/li/a/@href").getall()
        for ur in url2:
            ur='http://www.chinajiandu.cn'+ur
            yield scrapy.Request(ur,callback=self.Info,meta={"item":item})
    def Info(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//div[@class='title']/h1/text()").get().strip()
        collectionIntroduction=response.xpath("//div[@class='cont']/p/text()").getall()
        collectionImage=response.xpath("//div[@class='imgstyle imgfull']/a/img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item
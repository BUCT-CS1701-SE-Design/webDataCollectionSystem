import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection96Spider(scrapy.Spider):
    name = 'collection96'
    allowed_domains = ['gxmuseum.cn']
    start_urls = ['http://www.gxmuseum.cn/a/antique/index.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=96
        url1=response.xpath("//ul[@class='d3']/li/a/@href").getall()
        for url in url1:
            url='http://www.gxmuseum.cn'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        a=0
        url1=response.xpath("//ul[@class='d5 mt2']/li/a[1]/@href").getall()
        for url in url1:
            url='http://www.gxmuseum.cn'+url
            if a>5:
                break
            yield scrapy.Request(url,callback=self.Info,meta={"item":item})
            a+=1
    def Info(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//div[@class='title']/h2/text()").get().strip()
        collectionIntroduction=response.xpath("//div[@class='neirong']//text()").getall()
        collectionImage='http://www.gxmuseum.cn'+response.xpath("//div[@class='neirong']/ul//img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item
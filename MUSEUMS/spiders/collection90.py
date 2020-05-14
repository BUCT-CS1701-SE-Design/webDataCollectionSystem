import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection90Spider(scrapy.Spider):
    name = 'collection90'
    allowed_domains = ['gdmuseum.com']
    start_urls = ['http://www.gdmuseum.com/gdmuseum/_300746/_300758/index.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=90
        url1=response.xpath("//div[@class='column_list']//@href").getall()
        a=0
        for url in url1:
            url='http://www.gdmuseum.com'+url
            if a==3 or a==6 or a==7 or a==9 or a==11:
                a+=1
                continue
            a+=1
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        url2=response.xpath("//div[@class='js_cont']/div")
        a=0
        for link in url2:
            item=response.meta["item"]
            a+=1
            if a>10:
                break
            ur='http://www.gdmuseum.com'+link.xpath("./a[1]/@href").get()
            collectionImage='http://www.gdmuseum.com'+link.xpath("./a//@src").get()
            item['collectionImage']=collectionImage
            yield scrapy.Request(ur,callback=self.Info,meta={"item":item})
    def Info(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//div[@class='js_title show_title']//text()").getall()[1]
        collectionIntroduction=response.xpath("//div[@class='cont']//text()").getall()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        yield item
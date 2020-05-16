import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection83Spider(scrapy.Spider):
    name = 'collection83'
    allowed_domains = ['whmuseum.com.cn']
    start_urls = ['http://www.whmuseum.com.cn/collection'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=83
        print("qq"*20)
        url1=response.xpath("//div[@class='col-sort']/ul/li[1]/a/@href").getall()
        for url in url1:
            url='http://www.whmuseum.com.cn'+url
            print("*"*20)
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        url2=response.xpath("//ul[@id='photoviewer']/li[1]/a/@href").getall()
        a=0
        for ur in url2:
            ur='http://www.whmuseum.com.cn'+ur
            a+=1
            print("1"*20)
            if a>5:
                break
            yield scrapy.Request(ur,callback=self.Info,meta={"item":item})
    def Info(self,response):
        item=response.meta["item"]
        print("20"*20)
        collectionName=response.xpath("//*[@id='app']/div[2]//div[@class='cont']/h3/text()").get()
        collectionIntroduction=response.xpath("//*[@id='app']/div[2]//div[@class='cont']/div[3]//text()").getall()
        collectionImage=response.xpath("//div[@class='topbox']/div/img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item
import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection92Spider(scrapy.Spider):
    name = 'collection92'
    allowed_domains = ['sunyat-sen.org']
    start_urls = ['http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=71#'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=92
        url1=response.xpath("//div[@class='wwdc_pic']/a/@href").getall()
        for url in url1:
            url ='http://www.sunyat-sen.org'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        url2=response.xpath("//div[@class='ng_picbox']//p[1]//@href").getall()
        for ur in url2:
            yield scrapy.Request(ur,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
   
        collectionName=response.xpath("//h3[@class='conH3']/text()").get().strip()
        collectionIntroduction=response.xpath("//div[@class='contentBox']//text()").getall()
        Image1=response.xpath("//div[@class='zwpic']//@src").get()
        Image2=response.xpath("//div[@class='contentBox']//ul[1]//@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip().replace('\xa0','')
        if str(Image1).strip()=='':
            item['collectionImage']='http://www.sunyat-sen.org'+Image2
        else:
            item['collectionImage']='http://www.sunyat-sen.org'+Image1
        yield item
        # print(item)
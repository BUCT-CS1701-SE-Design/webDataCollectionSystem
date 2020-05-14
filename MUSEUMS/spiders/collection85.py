import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection80Spider(scrapy.Spider):
    name = 'collection85'
    allowed_domains = ['zhongshanwarship.org.cn']
    start_urls = ['http://www.zhongshanwarship.org.cn/wenwu.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=85
        url1=response.xpath("//div[@id='caseListDIV']/div//@href").getall()
        for url in url1:
            url='http://www.zhongshanwarship.org.cn/'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//h1[@id='zhanlanTitle']/text()").get()
        collectionIntroduction=response.xpath("//div[@id='infoContent']/p/span/text()").getall()
        collectionImage=response.xpath("//div[@class='cms-g']/div[2]/img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        print(item)